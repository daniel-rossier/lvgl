
include_directories(.)

add_executable(prof_test.elf prof_test.c)
target_compile_options(prof_test.elf PUBLIC -g)

add_library(prof_test_p.a STATIC prof_test_p.c)
target_compile_options(prof_test_p.a PRIVATE -pg)

target_link_libraries(prof_test.elf c)
target_link_libraries(prof_test.elf prof_test_p.a)
target_link_libraries(prof_test.elf lvgl)
