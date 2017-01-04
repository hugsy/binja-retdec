#
# Binary Ninja interface for RetDec decompiler
#
# Ref:
# * https://retdec.com/api/docs/decompiler.html
# * https://api.binary.ninja/
#
# @_hugsy_
#

from binaryninja import *
from retdec import RetDecDecompiler


def function_decompile(view, function_name):
    """Plugin callback for function decompilation."""
    bg_retdec = RetDecDecompiler(view, RetDecDecompiler.DECOMPILE_FUNCTION_MODE, function_name)
    bg_retdec.start()
    return


def bytes_decompile(self, addr, length):
    """Plugin callback for byte range decompilation."""
    bg_retdec = RetDecDecompiler(view, RetDecDecompiler.DECOMPILE_RANGE_MODE, addr, length)
    bg_retdec.start()
    return


def file_decompile(view):
    """Plugin callback for entire file decompilation."""
    bg_retdec = RetDecDecompiler(view, RetDecDecompiler.DECOMPILE_FILE_MODE)
    bg_retdec.start()
    return


PluginCommand.register_for_function("Decompile Function with RetDec",
                                    "Use RetDec decompiler to decompile the current function.",
                                    function_decompile)

# PluginCommand.register_for_range("Decompile selected range with RetDec",
#                                  "Use RetDec decompiler to decompile the selected bytes.",
#                                  bytes_decompile)

PluginCommand.register("Decompile Binary with RetDec",
                       "Use RetDec decompiler to decompile the binary.",
                       file_decompile)
