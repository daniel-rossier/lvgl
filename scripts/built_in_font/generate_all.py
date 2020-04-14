import os

print("Generating 12 px")
os.system("python built_in_font_gen.py --size 12 -o lv_font_montserrat_12.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_12.c')

print("\nGenerating 14 px")
os.system("python built_in_font_gen.py --size 14 -o lv_font_montserrat_14.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_14.c')

print("\nGenerating 16 px")
os.system("python built_in_font_gen.py --size 16 -o lv_font_montserrat_16.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_16.c')

print("\nGenerating 18 px")
os.system("python built_in_font_gen.py --size 18 -o lv_font_montserrat_18.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_18.c')

print("\nGenerating 20 px")
os.system("python built_in_font_gen.py --size 20 -o lv_font_montserrat_20.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_20.c')

print("\nGenerating 22 px")
os.system("python built_in_font_gen.py --size 22 -o lv_font_montserrat_22.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_22.c')

print("\nGenerating 24 px")
os.system("python built_in_font_gen.py --size 24 -o lv_font_montserrat_24.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_24.c')

print("\nGenerating 26 px")
os.system("python built_in_font_gen.py --size 26 -o lv_font_montserrat_26.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_26.c')

print("\nGenerating 28 px")
os.system("python built_in_font_gen.py --size 28 -o lv_font_montserrat_28.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_28.c')

print("\nGenerating 30 px")
os.system("python built_in_font_gen.py --size 30 -o lv_font_montserrat_30.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_30.c')

print("\nGenerating 32 px")
os.system("python built_in_font_gen.py --size 32 -o lv_font_montserrat_32.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_32.c')

print("\nGenerating 34 px")
os.system("python built_in_font_gen.py --size 34 -o lv_font_montserrat_34.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_34.c')

print("\nGenerating 36 px")
os.system("python built_in_font_gen.py --size 36 -o lv_font_montserrat_36.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_36.c')

print("\nGenerating 38 px")
os.system("python built_in_font_gen.py --size 38 -o lv_font_montserrat_38.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_38.c')

print("\nGenerating 40 px")
os.system("python built_in_font_gen.py --size 40 -o lv_font_montserrat_40.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_40.c')

print("\nGenerating 42 px")
os.system("python built_in_font_gen.py --size 42 -o lv_font_montserrat_42.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_42.c')

print("\nGenerating 44 px")
os.system("python built_in_font_gen.py --size 44 -o lv_font_montserrat_44.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_44.c')

print("\nGenerating 46 px")
os.system("python built_in_font_gen.py --size 46 -o lv_font_montserrat_46.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_46.c')

print("\nGenerating 48 px")
os.system("python built_in_font_gen.py --size 48 -o lv_font_montserrat_48.c --bpp 4")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_48.c')

print("\nGenerating 12 px subpx")
os.system("python built_in_font_gen.py --size 12 -o lv_font_montserrat_12_subpx.c --bpp 4 --subpx")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_12_subpx.c')

print("\nGenerating 28 px compressed")
os.system("python built_in_font_gen.py --size 28 -o lv_font_montserrat_28_compressed.c --bpp 4 --compressed")
os.system('sed -i \'s|#include "lvgl/lvgl.h"|#include "../../lvgl.h"|\' lv_font_montserrat_28_compressed.c')

