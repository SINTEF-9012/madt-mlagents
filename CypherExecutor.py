from typing import List
from autogen.coding import CodeBlock, CodeResult, CodeExtractor, MarkdownCodeExtractor, CodeExecutor
from IPython import get_ipython

from tools import run_query

class CypherCodeExecutor(CodeExecutor):
    """
    It extends a code executor to run cypher queries.
    This changes only the way a code block is executed, it will encapsulate the 
    code block with a run query function to be run in a jupyter environment.
    This is done because cypher execution is not supported by autogen, otherwise python 
    and jupyter are.
    """
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

        for code_block in code_blocks:
            result   = self._ipython.run_cell(f'''{run_query(f"""{code_block.code}""")}''')

            if result.result:
                exitcode = 0 if result.success else 1
                if result.error_before_exec:
                    log += f"\n{result.error_before_exec}"
                    exitcode = 1
                if result.error_in_exec:
                    log += f"\n{result.error_in_exec}"
                    exitcode = 1
        return CodeResult(exit_code=exitcode, output=log)