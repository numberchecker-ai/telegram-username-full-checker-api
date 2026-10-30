from pathlib import Path
import json, os, shutil, subprocess, sys, unittest
ROOT = Path(__file__).resolve().parents[1]
class RetiredContract(unittest.TestCase):
    def test_retired_examples_fail_without_credentials(self):
        manifest = json.loads((ROOT / "product.json").read_text())
        self.assertEqual(manifest["status"], "retired")
        self.assertEqual(manifest["endpoints"], {})
        env = dict(os.environ, GO111MODULE="off")
        env.pop("NUMBERCHECKER_API_KEY", None)
        commands = [[sys.executable, str(next(ROOT.glob("examples/python/*.py")))], ["bash", str(next(ROOT.glob("examples/shell/*.sh")))]]
        if shutil.which("node"): commands.append(["node", str(next(ROOT.glob("examples/nodejs/*.js")))])
        if shutil.which("go"): commands.append(["go", "run", str(next(ROOT.glob("examples/go/*.go")))])
        for command in commands:
            with self.subTest(command=command[0]):
                result = subprocess.run(command, env=env, capture_output=True, text=True, timeout=60)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("retired", result.stdout + result.stderr)
