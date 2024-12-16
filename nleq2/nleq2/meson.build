nleq2_wrappers = custom_target(
  'nleq2module.c',
  input : ['nleq2.pyf'],
  output : ['nleq2module.c', 'nleq2-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)

nleq2_lib = static_library('nleq2_lib',
  'nleq2.f',
  'linalg_nleq2.f',
  'zibmon.f',
  'zibsec.f',
  'zibconst.f',
  'wnorm.f',
  fortran_args: [fortran_ignore_warnings],
  override_options: ['b_lto=false'],
  gnu_symbol_visibility: 'hidden',
)

py.extension_module(
  'nleq2',
  nleq2_wrappers,
#  'nleq2module.c',
  link_with: [nleq2_lib],
  c_args: [Wno_unused_variable],
  dependencies: [lapack, fortranobject_dep],
  install: true,
  link_language: 'fortran',
  include_directories: inc_np,
  subdir: 'nleq2/nleq2'
)

#py.install_sources(
#  [
#    '__init__.py'
#  ],
#  subdir: 'nleq2/nleq2'
#)

install_data(
  ['nleq2_readme.txt', 'readme.txt'],
  install_dir: nleq2_dir / 'nleq2'
)
