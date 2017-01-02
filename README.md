# RetDec Decompiler (v0.1)
Author: **hugsy**

_Binary Ninja plugin to decompile binaries using RetDec API._

## Description:

This plugin aims to bind together Binary Ninja disassembly with the Retargetable Decompiler (RetDec - https://retdec.com) to decompile binary files, functions, or even byte range into pseudo-C code.
This script also improves the result from RetDec by augmenting the pseudo C code with the symbol names found (or created) within the Binary Ninja session.

![binja-retdec](http://i.imgur.com/E1RURpo.png)


## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

 * dev - 1.0.dev-576
 * release - 9999


## Required Dependencies

The following dependencies are required for this plugin:

 * pip - requests


## License

This plugin is released under a [MIT](LICENSE) license.
