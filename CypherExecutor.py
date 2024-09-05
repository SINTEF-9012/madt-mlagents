from typing import List
from autogen.coding import CodeBlock, CodeResult, CodeExtractor, MarkdownCodeExtractor, CodeExecutor
from IPython import get_ipython

from tools import run_query

class CypherCodeExecutor(CodeExecutor):

    @property
    def code_extractor(self) -> CodeExtractor:
        # Extact code from markdown blocks.
        return MarkdownCodeExtractor()

    def __init__(self) -> None:
        # Get the current IPython instance running in this notebook.
        self._ipython = get_ipython()

    def execute_code_blocks(self, code_blocks: List[CodeBlock]) -> CodeResult:
        log = ""
        exitcode = 1
        result   = self._ipython.run_cell(run_query(f"""{code_blocks[0].code}""") )

        if result.result:
            exitcode = 0 if result.success else 1
            if result.error_before_exec:
                log += f"\n{result.error_before_exec}"
                exitcode = 1
            if result.error_in_exec:
                log += f"\n{result.error_in_exec}"
                exitcode = 1
        return CodeResult(exit_code=exitcode, output=log)