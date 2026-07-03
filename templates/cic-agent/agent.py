"""
CIC Agent Template
==================
Drop-in template for a CIC-compliant agent. Implements the full phase chain
per AGENTS.md Section 11. Implements all six Forge Field principles.

Usage:
  1. Copy directory to agents/<domain>/<agent_name>/
  2. Replace all PLACEHOLDER comments.
  3. Implement _execute_core() with your agent's logic.
  4. Sync agent.manifest.yaml phases/permissions with your implementation.
  5. Run: pytest tests/ -v && pytest tests/ --cov=agent --cov-report=term-missing
  6. Register: cic agent register ./agent.manifest.yaml
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Any

from cic.runtime import (
    AgentManifest, CheckpointRecord, FatalFailure, InputEnvelope,
    OutputEnvelope, RecoverableFailure, StateManager, ToolResult, cic,
)


# ── Data classes ──────────────────────────────────────────────────────────────

@dataclass
class ValidatedInput:
    query: str
    session_id: str
    user_id: str
    trace_id: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class CandidateOutput:
    # PLACEHOLDER: Replace with fields specific to your agent's output.
    result: Any = None
    tool_results: dict[str, Any] = field(default_factory=dict)


# ── Agent ─────────────────────────────────────────────────────────────────────

class CICAgentTemplate:
    """
    CIC-compliant agent template.
    Manifest ID: cic.agents.<domain>.<agent_name>
    """

    def __init__(self, manifest: AgentManifest, state: StateManager) -> None:
        self.manifest = manifest
        self.state = state

    # ── Phase: validate ───────────────────────────────────────────────────────
    # Reads:  inputs.raw
    # Writes: inputs.validated | errors.validate

    def validate(self) -> bool:
        raw: dict[str, Any] = self.state.read("inputs.raw", phase="validate")
        errors: list[dict] = []

        if not raw.get("query") or not raw["query"].strip():
            errors.append({
                "code": "ERR_VALIDATE_MISSING_REQUIRED", "field": "query",
                "message": "Required field 'query' is absent or empty.",
                "severity": "recoverable", "retry_eligible": False,
                "docs_url": "https://cic.internal/agents/errors/ERR_VALIDATE_MISSING_REQUIRED",
            })

        context = raw.get("context", {})
        for field_name in ("session_id", "user_id"):
            if not context.get(field_name):
                errors.append({
                    "code": "ERR_VALIDATE_MISSING_REQUIRED",
                    "field": f"context.{field_name}",
                    "message": f"Required field 'context.{field_name}' is absent.",
                    "severity": "recoverable", "retry_eligible": False,
                    "docs_url": "https://cic.internal/agents/errors/ERR_VALIDATE_MISSING_REQUIRED",
                })

        # PLACEHOLDER: Add agent-specific validation rules here.

        if errors:
            self.state.write("errors.validate", errors, phase="validate")
            self.state.write("checkpoints.validate", self.state.checkpoint("validate"), phase="validate")
            return False

        validated = ValidatedInput(
            query=raw["query"].strip(),
            session_id=context["session_id"],
            user_id=context["user_id"],
            trace_id=raw.get("trace_id") or str(uuid.uuid4()),
            metadata=raw.get("metadata", {}),
        )
        self.state.write("inputs.validated", validated, phase="validate")
        self.state.write("checkpoints.validate", self.state.checkpoint("validate"), phase="validate")
        return True

    # ── Phase: plan ───────────────────────────────────────────────────────────
    # OPTIONAL — uncomment if agent calls more than one tool
    # Reads:  inputs.validated
    # Writes: plan.tool_sequence

    # def plan(self) -> None:
    #     validated: ValidatedInput = self.state.read("inputs.validated", phase="plan")
    #     tool_sequence = [
    #         {"step": 1, "tool": "cic.tool.search",    "params": {"query": validated.query}, "depends_on": []},
    #         {"step": 2, "tool": "cic.tool.retrieval", "params": {"doc_ids": "__from_step_1__"}, "depends_on": [1]},
    #     ]
    #     self.state.write("plan.tool_sequence", tool_sequence, phase="plan")
    #     self.state.write("checkpoints.plan", self.state.checkpoint("plan"), phase="plan")

    # ── Phase: execute ────────────────────────────────────────────────────────
    # Reads:  inputs.validated [, plan.tool_sequence]
    # Writes: execute.tool_results, execute.candidate_outputs

    def execute(self) -> None:
        validated: ValidatedInput = self.state.read("inputs.validated", phase="execute")
        tool_results: dict[str, Any] = {}

        # PLACEHOLDER: Add tool calls here.
        # search_result = self._call_tool("cic.tool.search", {"query": validated.query}, phase="execute")
        # tool_results["search"] = search_result.data

        candidate = self._execute_core(validated, tool_results)
        self.state.write("execute.tool_results", tool_results, phase="execute")
        self.state.write("execute.candidate_outputs", candidate, phase="execute")
        self.state.write("checkpoints.execute", self.state.checkpoint("execute"), phase="execute")

    def _execute_core(self, validated: ValidatedInput, tool_results: dict[str, Any]) -> CandidateOutput:
        """
        PLACEHOLDER: Implement your agent's core reasoning here.
        Read from `validated` and `tool_results`. Return a CandidateOutput.
        Must be pure — do not write to state directly.
        """
        return CandidateOutput(result={"echo": validated.query}, tool_results=tool_results)

    # ── Phase: review ─────────────────────────────────────────────────────────
    # OPTIONAL — uncomment for high-stakes outputs
    # Reads:  execute.candidate_outputs
    # Writes: review.approved_outputs | review.issues

    # def review(self) -> bool:
    #     candidate: CandidateOutput = self.state.read("execute.candidate_outputs", phase="review")
    #     issues: list[str] = []
    #     # PLACEHOLDER: Add consistency checks here.
    #     if issues:
    #         self.state.write("review.issues", issues, phase="review")
    #         self.state.write("checkpoints.review", self.state.checkpoint("review"), phase="review")
    #         return False
    #     self.state.write("review.approved_outputs", candidate, phase="review")
    #     self.state.write("checkpoints.review", self.state.checkpoint("review"), phase="review")
    #     return True

    # ── Phase: emit ───────────────────────────────────────────────────────────
    # Reads:  execute.candidate_outputs [, review.approved_outputs]
    # Writes: emit.final_output, checkpoints.emit

    def emit(self) -> OutputEnvelope:
        candidate: CandidateOutput = self.state.read("execute.candidate_outputs", phase="emit")
        validated: ValidatedInput = self.state.read("inputs.validated", phase="emit")

        output = OutputEnvelope(
            status="success",
            agent_id=self.manifest.id,
            invocation_id=self.state.read("meta.invocation_id", phase="emit"),
            phase_trace=self.state.read("meta.phase_trace", phase="emit"),
            result=candidate.result,          # PLACEHOLDER: Map to your output schema
            metadata=validated.metadata or None,
        )
        self.state.write("emit.final_output", output.to_dict(), phase="emit")
        self.state.write("checkpoints.emit", self.state.checkpoint("emit"), phase="emit")
        return output

    # ── Tool call helper (§ 11.7.2) ───────────────────────────────────────────

    def _call_tool(self, tool_id: str, params: dict, phase: str) -> ToolResult:
        """Permission-asserting, timeout-enforcing, error-classifying tool wrapper."""
        self.state._assert_call_permitted(tool_id, phase)
        try:
            result = cic.tool.call(tool_id=tool_id, params=params, timeout_ms=self.manifest.slo.timeout_ms)
            self.state.write(f"execute.tool_calls.{tool_id.replace('.', '_')}.result", result.to_dict(), phase=phase)
            return result
        except cic.tool.TimeoutError:
            raise RecoverableFailure(code="ERR_TOOL_TIMEOUT",
                message=f"Tool '{tool_id}' exceeded timeout of {self.manifest.slo.timeout_ms}ms.")
        except cic.tool.PermissionError:
            raise FatalFailure(code="ERR_AUTH_TOOL_FORBIDDEN",
                message=f"Manifest does not grant call permission for '{tool_id}'.")
        except cic.tool.ToolError as exc:
            raise RecoverableFailure(code="ERR_TOOL_INTERNAL",
                message=f"Tool '{tool_id}' returned an error: {exc.code}")


# ── Router (§ 11.2.2) ─────────────────────────────────────────────────────────

class AgentRouter:
    """Entry point for all agent invocations. Contains NO business logic."""

    def __init__(self, manifest: AgentManifest) -> None:
        self.manifest = manifest

    def invoke(self, envelope: InputEnvelope) -> OutputEnvelope:
        invocation_id = str(uuid.uuid4())
        state = StateManager(agent_id=self.manifest.id, manifest=self.manifest, invocation_id=invocation_id)
        state.write("meta.invocation_id", invocation_id, phase="router")
        state.write("meta.phase_trace", [], phase="router")
        state.write("inputs.raw", envelope.to_dict(), phase="router")

        agent = CICAgentTemplate(manifest=self.manifest, state=state)

        try:
            self._record_phase("validate", state)
            if not agent.validate():
                return self._emit_validation_error(state, invocation_id)

            # Uncomment if plan phase is active:
            # self._record_phase("plan", state); agent.plan()

            self._record_phase("execute", state)
            agent.execute()

            # Uncomment if review phase is active:
            # for attempt in range(self.manifest.slo.max_retries + 1):
            #     self._record_phase("review", state)
            #     if agent.review(): break
            #     if attempt == self.manifest.slo.max_retries:
            #         return self._emit_error(state, invocation_id, "ERR_REVIEW_MAX_RETRIES",
            #             "Review phase failed after max retries.", "fatal", retry_eligible=False)
            #     self._record_phase("execute", state); agent.execute()

            self._record_phase("emit", state)
            return agent.emit()

        except RecoverableFailure as exc:
            return self._emit_error(state, invocation_id, exc.code, exc.message, "recoverable", retry_eligible=True)
        except FatalFailure as exc:
            return self._emit_error(state, invocation_id, exc.code, exc.message, "fatal", retry_eligible=False)
        except Exception as exc:
            cic.logger.critical("Unhandled exception", agent_id=self.manifest.id,
                invocation_id=invocation_id, exc_info=exc)
            return self._emit_error(state, invocation_id, "ERR_UNKNOWN_UNHANDLED_EXCEPTION",
                "An internal error occurred. The incident has been logged.", "fatal", retry_eligible=False)

    def _record_phase(self, phase: str, state: StateManager) -> None:
        trace: list[str] = state.read("meta.phase_trace", phase="router")
        trace.append(phase)
        state.write("meta.phase_trace", trace, phase="router")

    def _emit_validation_error(self, state: StateManager, invocation_id: str) -> OutputEnvelope:
        errors = state.read("errors.validate", phase="router")
        primary = (errors or [{"code": "ERR_VALIDATE_UNKNOWN", "message": "Validation failed.",
                                "severity": "recoverable"}])[0]
        return OutputEnvelope(status="error", agent_id=self.manifest.id,
            invocation_id=invocation_id,
            phase_trace=state.read("meta.phase_trace", phase="router"), error=primary)

    def _emit_error(self, state, invocation_id, code, message, severity, retry_eligible) -> OutputEnvelope:
        return OutputEnvelope(status="error", agent_id=self.manifest.id, invocation_id=invocation_id,
            phase_trace=state.read("meta.phase_trace", phase="router"),
            error={"code": code, "message": message, "severity": severity,
                   "retry_eligible": retry_eligible,
                   "docs_url": f"https://cic.internal/agents/errors/{code}"})


def create_router(manifest: AgentManifest) -> AgentRouter:
    """Factory called by the CIC runtime to instantiate the agent router."""
    return AgentRouter(manifest=manifest)
