# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
#flags = [
#'-Wall',
#'-Wextra',
#'-Werror',
#'-Wc++98-compat',
#'-Wno-long-long',
#'-Wno-variadic-macros',
#'-fexceptions',
#'-DNDEBUG',
#'-DUSE_CLANG_COMPLETER',
## THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
## language to use when compiling headers. So it will guess. Badly. So C++
## headers will be compiled as C headers. You don't want that so ALWAYS specify
## a "-std=<something>".
## For a C project, you would set this to something like 'c99' instead of
## 'c++11'.    }

##'-std=c++11',
## ...and the same thing goes for the magic -x option which specifies the
## language that the files to be compiled are written in. This is mostly
## relevant for c++ headers.
## For a C project, you would set this to 'c' instead of 'c++'.
#'-x',
#'c++',
#'-isystem',
#'../BoostParts',
#'-isystem',
## This path will only work on OS X, but extra paths that don't exist are not
## harmful
#'/System/Library/Frameworks/Python.framework/Headers',
#'-isystem',
#'../llvm/include',
#'-isystem',
#'../llvm/tools/clang/include',
#'-I',

#'.',
#'-I',
#'./ClangCompleter',
#'-isystem',
#'./tests/gmock/gtest',
#'-isystem',
#'./tests/gmock/gtest/include',
#'-isystem',
#'./tests/gmock',
#'-isystem',
#'./tests/gmock/include'
#]
flags = []

# Defaults, if no database can be found.
defaultsc = [
        'gcc',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-pthread'
        '-std=c99',
        ]
defaultscpp = [
        'c++',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-pthread'
        '-std=c++11',
        ]

# Things that must be included.
entered_flags = ['-fdelayed-template-parsing']

#
def DirectoryOfThisScript():
    return os.path.dirname( os.path.abspath( __file__ ) )

# Find all compilation databases in the build directory and load them.

def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def FlagsForFile( filename ):
    # Search through all parent directories for a directory named 'build'
    databases = []
    path_focus = os.path.dirname(filename)
    while len(path_focus) > 1:
        for f in os.listdir(path_focus):
            if f == 'build':
                compilation_database_folder = path_focus + "/" + f
                for r,d,f in os.walk(compilation_database_folder):
                    for files in f:
                        if files == 'compile_commands.json':
                            databases += [ycm_core.CompilationDatabase( r )]
        path_focus = os.path.dirname(os.path.dirname(path_focus))

    # Use a header's source file database for completion.
    filetype_flags = []
    if filename.endswith(".h"):
        for f in os.listdir(os.path.dirname(filename)):
            if filename.replace(".h",".cpp").find(f) != -1:
                filename = filename.replace(".h",".cpp")
                break
            if filename.replace(".h",".c").find(f) != -1:
                filename = filename.replace(".h",".c")
                break
    elif filename.endswith(".hpp"):
        for f in os.listdir(os.path.dirname(filename)):
            if filename.replace(".hpp",".cpp").find(f) != -1:
                filename = filename.replace(".hpp",".cpp")
                break

    # Get the compile commands
    final_flags = []
    # If possible, from the database.
    if len(databases) > 0:
        for database in databases:
            compilation_info = database.GetCompilationInfoForFile( filename )
            fromfile_flags = MakeRelativePathsInFlagsAbsolute(
            compilation_info.compiler_flags_,
            compilation_info.compiler_working_dir_ )
            final_flags += fromfile_flags

    # If not, set some sane defaults.
    else:
        relative_to = DirectoryOfThisScript()
        final_flags += MakeRelativePathsInFlagsAbsolute( flags, relative_to )
    if not final_flags:
        if filename.endswith(".c"):
            final_flags = defaultsc
        elif filename.endswith(".cpp"):
            final_flags = defaultscpp

    # This allows header files to be parsed according to their parent source
    final_flags = filetype_flags + final_flags

    # For things that must be included regardless:
    final_flags += entered_flags
    return {
        'flags': final_flags,
        'do_cache': True
    }
