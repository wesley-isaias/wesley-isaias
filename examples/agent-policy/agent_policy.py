"""Illustrative, dependency-free policy gate for an AI tool request.

This is a standalone educational example, NOT Zayuni MCP production code.
"""
from dataclasses import dataclass
from pathlib import PurePosixPath

ALLOWED_ACTIONS = frozenset({"read_file", "list_directory", "run_tests"})
BLOCKED_PARTS = frozenset({".git", ".env", "secrets", "credentials", "private"})


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str


def authorize(action: str, path: str) -> Decision:
    """Deny by default; never execute commands or access files."""
    if action not in ALLOWED_ACTIONS:
        return Decision(False, "action_not_allowed")
    if not isinstance(path, str) or not path.startswith("/workspace/"):
        return Decision(False, "outside_workspace")
    if "\\" in path or "\x00" in path:
        return Decision(False, "invalid_path")
    parts = PurePosixPath(path).parts
    if ".." in path.split("/") or any(part.lower() in BLOCKED_PARTS for part in parts):
        return Decision(False, "sensitive_or_traversal_path")
    if action == "run_tests" and path != "/workspace/tests":
        return Decision(False, "tests_directory_only")
    return Decision(True, "policy_allowed")
