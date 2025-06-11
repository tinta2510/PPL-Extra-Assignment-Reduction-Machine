# Reduction Machine – PPL Assignment
## Overview
This project is an implementation of a virtual machine using reduction rules. The virtual machine reads a program written in prefix notation, interprets it using **Prolog**, and simulates execution based on the syntax and semantics defined in the assignment specification ([docs/BaiTapLonMR-1.3.pdf](docs/BaiTapLonMR-1.3.pdf)).

This project aims to enhance understanding of **logic programming** and how fundamental programming constructs (like expressions, function calls, and control structures) are executed at a low level.

## File Structure
- `vm.pl`: The Prolog implementation of the virtual machine.
- `virtual.pl`: trigger vm.pl
- `VMSuite.py`: Python script that runs the virtual machine and tests it against testcases.

## Getting Started
### Prerequisites
- **SWI-Prolog**: Ensure that SWI-Prolog is installed and available in your PATH.
- **Python 3.x**: Make sure you have Python 3 installed.
- **Python package**: Install the `swiplserver` package using pip:
  ```bash
  pip install swiplserver
  ```
### Setup Instructions
1. Navigate to the project directory:
   ```bash
   cd assignment-initial/src
   ```
2. Run the test suite:
   ```bash
   python run.py test VMSuite
   ```

## Features
### Declarations
Supports `var`, `const`, `par`, `func`, and `proc` declarations.
### Expressions
Handles:
- **Arithmetic**: `add`, `sub`, `times`, `rdiv`, `idiv`, `imod`
- **Boolean**: `band`, `bor`, `bnot`
- **Relational**: `greater`, `less`, `eql`, `ne`, etc.
- **Function calls**: `call(...)`
### Statements
Supports:
- `assign`, `block`, `if`, `while`, `do`, `loop`, `call`
- Control flow: `break(null)`, `continue(null)`
### Built-in Functions and Procedures
Procedures: `writeInt`, `writeIntLn`, `writeReal`, `writeBool`, `writeStr`, `writeLn`, etc.
Functions: `readInt`, `readReal`, `readBool`
## Error Handling
Handles various runtime exceptions, such as:
- `redeclare_identifier`
- `undeclare_identifier`
- `type_mismatch`
- `wrong_number_of_arguments`       
- `invalid_expression`
- `undeclare_function`
- `undeclare_procedure`
- `break_not_in_loop`
- `continue_not_in_loop`
- `cannot_assign`

## Change Log
This is version 1.3
Change current directory to initial/src where there is file run.py
Type: python run.py test VMSuite
Change log
- From 1.0
Change minus to sub in vm.pl and VMSuite.py
- From 1.1
Change the type from real to float in test 403 
Change method TestVM.check in TestUtils.py so that it saves input string to files in folder testcases
Add the version of function getAndTest in run.py for the new version of Python
- From 1.2
Break vm.pl into virtual.pl and vm.pl
Change TestUtil.py such that starting from virtual.pl




