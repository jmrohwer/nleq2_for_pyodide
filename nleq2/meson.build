mymodule_dir = py.get_install_dir() / 'mfm'

py.install_sources([
    '__init__.py'
  ],
  subdir: 'mfm'
)

pure_subdirs = [
    'tests'
]

foreach subdir: pure_subdirs
  install_subdir(subdir, install_dir: mymodule_dir, install_tag: 'python-runtime')
endforeach

Wno_unused_variable = cc.get_supported_arguments('-Wno-unused-variable')

# Fortran warning flags
_fflag_Wno_argument_mismatch = ff.get_supported_arguments('-Wno-argument-mismatch')
_fflag_Wno_conversion = ff.get_supported_arguments('-Wno-conversion')
_fflag_Wno_maybe_uninitialized = ff.get_supported_arguments('-Wno-maybe-uninitialized')
_fflag_Wno_unused_dummy_argument = ff.get_supported_arguments('-Wno-unused-dummy-argument')
_fflag_Wno_unused_label = ff.get_supported_arguments('-Wno-unused-label')
_fflag_Wno_unused_variable = ff.get_supported_arguments('-Wno-unused-variable')
_fflag_Wno_tabs = ff.get_supported_arguments('-Wno-tabs')
# The default list of warnings to ignore from Fortran code. There is a lot of
# old, vendored code that is very bad and we want to compile it silently (at
# least with GCC and Clang)
fortran_ignore_warnings = ff.get_supported_arguments(
 _fflag_Wno_argument_mismatch,
 _fflag_Wno_conversion,
 _fflag_Wno_maybe_uninitialized,
 _fflag_Wno_unused_dummy_argument,
 _fflag_Wno_unused_label,
 _fflag_Wno_unused_variable,
 _fflag_Wno_tabs,
)

numpy_nodepr_api = ['-DNPY_NO_DEPRECATED_API=NPY_1_9_API_VERSION']

fortranobject_lib = static_library('_fortranobject',
  fortranobject_c,
  c_args: numpy_nodepr_api,
  dependencies: py_dep,
  include_directories: inc_np,
  gnu_symbol_visibility: 'hidden',
)

fortranobject_dep = declare_dependency(
  link_with: fortranobject_lib,
  include_directories: inc_np,
)

subdir('fmath')
