#!/usr/bin/python
# coding=UTF-8
# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons
import re;
import os;

# File extensions{{{
# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
    'eot'          : '',
    'svg'          : '',
    'woff'         : '',
    'styl'         : '',
    'scss'         : '',
    'htm'          : '',
    'html'         : '',
    'njk'          : '',
    'slim'         : '',
    'ejs'          : '',
    'css'          : '',
    'less'         : '',
    'md'           : '',
    'markdown'     : '',
    'json'         : '',
    'graphql'      : '',
    'js'           : '',
    'jsx'          : '',
    'rb'           : '',
    'php'          : '',
    'py'           : '',
    'pyc'          : '',
    'pyo'          : '',
    'pyd'          : '',
    'coffee'       : '',
    'mustache'     : '',
    'hbs'          : '',
    'conf'         : '',
    'ini'          : '',
    'yml'          : '',
    'bat'          : '',
    'jpg'          : '',
    'jpeg'         : '',
    'bmp'          : '',
    'png'          : '',
    'gif'          : '',
    'ico'          : '',
    'twig'         : '',
    'cpp'          : '',
    'c++'          : '',
    'cxx'          : '',
    'cc'           : '',
    'cp'           : '',
    'c'            : '',
    'hs'           : '',
    'lhs'          : '',
    'lua'          : '',
    'java'         : '',
    'sh'           : '',
    'zsh'          : '',
    'ml'           : 'λ',
    'mli'          : 'λ',
    'diff'         : '',
    'db'           : '',
    'sql'          : '',
    'dump'         : '',
    'clj'          : '',
    'cljc'         : '',
    'cljs'         : '',
    'edn'          : '',
    'scala'        : '',
    'go'           : '',
    'dart'         : '',
    'xul'          : '',
    'sln'          : '',
    'suo'          : '',
    'pl'           : '',
    'pm'           : '',
    't'            : '',
    'rss'          : '',
    'f#'           : '',
    'fsscript'     : '',
    'fsx'          : '',
    'fs'           : '',
    'fsi'          : '',
    'rs'           : '',
    'rlib'         : '',
    'd'            : '',
    'erl'          : '',
    'hrl'          : '',
    'vim'          : '',
    'vimrc'        : '',
    'ai'           : '',
    'psd'          : '',
    'psb'          : '',
    'ts'           : '',
    'jl'           : '',
    'rc'           : '',
    'xml'          : '',
    'log'          : '',
    'avi'          : '',
    'mov'          : '',
    'mpeg'         : '',
    'mpg'          : '',
    'mkv'          : '',
    'flv'          : '',
    'mp4'          : '',
    'mp3'          : '',
    'flac'         : '',
    'wav'          : '',
    'ogg'          : '',
    'swap'         : '',
    'epub'         : '',
    'pdf'          : '',
    '7z'           : '',
    'apk'          : '',
    'bz2'          : '',
    'cab'          : '',
    'cpio'         : '',
    'deb'          : '',
    'gem'          : '',
    'gz'           : '',
    'gzip'         : '',
    'lha'          : '',
    'lzh'          : '',
    'lzma'         : '',
    'rar'          : '',
    'rpm'          : '',
    'tar'          : '',
    'tgz'          : '',
    'xz'           : '',
    'zip'          : '',
    'lock'         : '',
    'orig'         : '',
    'temp'         : '',
    'tmp'          : '',
}
# }}}
# Directories matches {{{
dir_node_exact_matches = {
# English
    '.git'                             : '',
    'node_modules'                     : '',
    'code'                             : '',
    'Desktop'                          : '',
    'Documents'                        : '',
    'Downloads'                        : '',
    'Pictures'                         : '',
}
# }}}
# File matches {{{
file_node_exact_matches = {
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'gruntfile.coffee'                 : '',
    'gruntfile.js'                     : '',
    'gruntfile.ls'                     : '',
    'gulpfile.coffee'                  : '',
    'gulpfile.js'                      : '',
    'gulpfile.ls'                      : '',
    'Gemfile'                          : '',
    'dropbox'                          : '',
    'favicon.ico'                      : '',
    'LICENSE'                          : '',
    'license'                          : '',
    'license.txt'                      : '',
    'react.jsx'                        : '',
    'package-lock.json'                : '',
    '.DS_Store'                        : '',
    'npm-error.log'                    : '',
    'yarn-error.log'                   : '',
    'procfile'                         : '',
    '.git'                             : '',
    '.apollo-engine.json'              : '',
    '.babelrc'                         : '',
    '.babelrc'                         : '',
    '.bashprofile'                     : '',
    '.bashrc'                          : '',
    'config'                           : '',
    '.dmrc'                            : '',
    'Dockerfile'                       : '',
    '.dockerignore'                    : '',
    '.ds_store'                        : '',
    'ecosystem.json'                   : '',
    '.editorconfig'                    : '',
    'editorconfig'                     : '',
    '.env'                             : '',
    '.eslintignore'                    : '',
    '.eslintrc.js'                     : '',
    '.fasd'                            : '',
    '.flowconfig'                      : '',
    '.gitattributes'                   : '',
    '.gitconfig'                       : '',
    '.gitconfig'                       : '',
    '.gitignore'                       : '',
    '.gitkeep'                         : '',
    '.gitmodules'                      : '',
    '.htaccess'                        : '',
    'ini'                              : '',
    '.jack-settings'                   : '',
    'jsdoc.json'                       : '',
    'manifest.json'                    : '',
    'mimeapps.list'                    : '',
    '.mime.types'                      : '',
    'nodemon.json'                     : '',
    '.npmignore'                       : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    'Rakefile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.tern-project'                    : '',
    'user-dirs.dirs'                   : '',
    'webpack.config.js'                : '',
    '.Xdefaults'                       : '',
    '.xinputrc'                        : '',
    '.Xresources'                      : '',
    '.zshrc'                           : '',
    '.vimrc'                           : '',
    '.viminfo'                         : '',
    '.viminfo'                         : '',
    'package.json'                     : '',
}
# }}}

def devicon(file):
  if file.is_directory: return dir_node_exact_matches.get(file.relative_path, '')
  return file_node_exact_matches.get(file.relative_path, file_node_extensions.get(file.extension, ''))

# vim:foldmethod=marker:foldlevel=0
