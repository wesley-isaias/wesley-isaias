import unittest

from agent_policy import authorize


class AgentPolicyTests(unittest.TestCase):
    def test_safe_read(self):
        self.assertTrue(authorize("read_file", "/workspace/src/main.py").allowed)

    def test_safe_list(self):
        self.assertTrue(authorize("list_directory", "/workspace/docs").allowed)

    def test_tests_only_in_tests_dir(self):
        self.assertTrue(authorize("run_tests", "/workspace/tests").allowed)
        self.assertFalse(authorize("run_tests", "/workspace/src").allowed)

    def test_mutations_denied(self):
        for action in ("delete_file", "deploy", "run_shell", "write_file"):
            with self.subTest(action=action):
                self.assertFalse(authorize(action, "/workspace/src").allowed)

    def test_sensitive_paths_denied(self):
        for path in ("/workspace/.env", "/workspace/.git/config",
                     "/workspace/secrets/key", "/workspace/PRIVATE/data"):
            with self.subTest(path=path):
                self.assertFalse(authorize("read_file", path).allowed)

    def test_traversal_denied(self):
        self.assertFalse(authorize("read_file", "/workspace/src/../../etc/passwd").allowed)

    def test_outside_workspace_denied(self):
        self.assertFalse(authorize("read_file", "/etc/passwd").allowed)

    def test_windows_separator_denied(self):
        self.assertFalse(authorize("read_file", "/workspace/src\\..\\secrets").allowed)

    def test_null_byte_denied(self):
        self.assertFalse(authorize("read_file", "/workspace/src/\x00key").allowed)

    def test_unknown_and_empty_inputs(self):
        self.assertFalse(authorize("", "/workspace/src").allowed)
        self.assertFalse(authorize("read_file", "").allowed)


if __name__ == "__main__":
    unittest.main()
