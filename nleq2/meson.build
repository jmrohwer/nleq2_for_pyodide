nleq2_dir = py.get_install_dir() / 'nleq2'

py.install_sources([
    '__init__.py'
  ],
  subdir: 'nleq2'
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

subdir('nleq2')
