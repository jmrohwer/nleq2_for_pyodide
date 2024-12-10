project('mfm',
        ['c', 'fortran'],
        version : '1.0.4',
        meson_version: '>= 1.2.3'
)

py = import('python').find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  ['-c', 'import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = incdir_numpy / '..' / '..' / 'f2py' / 'src'
fortranobject_c = incdir_f2py / 'fortranobject.c'

inc_np = include_directories(incdir_numpy, incdir_f2py)

cc = meson.get_compiler('c')
ff = meson.get_compiler('fortran')
if ff.has_argument('-Wno-conversion')
  add_project_arguments('-Wno-conversion', language: 'fortran')
endif

subdir('mfm')