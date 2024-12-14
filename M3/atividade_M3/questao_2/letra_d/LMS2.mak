# Generated by the VisualDSP++ IDDE

# Note:  Any changes made to this Makefile will be lost the next time the
# matching project file is loaded into the IDDE.  If you wish to preserve
# changes, rename this file and run it externally to the IDDE.

# The syntax of this Makefile is such that GNU Make v3.77 or higher is
# required.

# The current working directory should be the directory in which this
# Makefile resides.

# Supported targets:
#     LMS2_Debug
#     LMS2_Debug_clean

# Define this variable if you wish to run this Makefile on a host
# other than the host that created it and VisualDSP++ may be installed
# in a different directory.

ADI_DSP=C:\Program Files (x86)\Analog Devices\VisualDSP 5.1.2


# $VDSP is a gmake-friendly version of ADI_DIR

empty:=
space:= $(empty) $(empty)
VDSP_INTERMEDIATE=$(subst \,/,$(ADI_DSP))
VDSP=$(subst $(space),\$(space),$(VDSP_INTERMEDIATE))

RM=cmd /C del /F /Q

#
# Begin "LMS2_Debug" configuration
#

ifeq ($(MAKECMDGOALS),LMS2_Debug)

LMS2_Debug : ./Debug/LMS2.dxe 

Debug/lms_process.doj :lms_process.c $(VDSP)/Blackfin/include/stdio.h $(VDSP)/Blackfin/include/yvals.h 
	@echo ".\lms_process.c"
	$(VDSP)/ccblkfn.exe -c .\lms_process.c -file-attr ProjectName=LMS2 -g -structs-do-not-overlap -no-multiline -D DO_CYCLE_COUNTS -double-size-32 -decls-strong -warn-protos -proc ADSP-BF533 -o .\Debug\lms_process.doj -MM

Debug/main.doj :main.c $(VDSP)/Blackfin/include/stdio.h $(VDSP)/Blackfin/include/yvals.h $(VDSP)/Blackfin/include/stdlib.h $(VDSP)/Blackfin/include/stdlib_bf.h $(VDSP)/Blackfin/include/math.h $(VDSP)/Blackfin/include/ymath.h $(VDSP)/Blackfin/include/math_bf.h $(VDSP)/Blackfin/include/fract_typedef.h $(VDSP)/Blackfin/include/fract_math.h $(VDSP)/Blackfin/include/ccblkfn.h $(VDSP)/Blackfin/include/builtins.h $(VDSP)/Blackfin/include/sys/builtins_support.h $(VDSP)/Blackfin/include/fr2x16_typedef.h $(VDSP)/Blackfin/include/r2x16_typedef.h $(VDSP)/Blackfin/include/raw_typedef.h $(VDSP)/Blackfin/include/sys/anomaly_macros_rtl.h $(VDSP)/Blackfin/include/sys/mc_typedef.h $(VDSP)/Blackfin/include/fr2x16_math.h $(VDSP)/Blackfin/include/fr2x16_base.h $(VDSP)/Blackfin/include/r2x16_base.h $(VDSP)/Blackfin/include/cycles.h $(VDSP)/Blackfin/include/xcycle_count.h $(VDSP)/Blackfin/include/limits.h $(VDSP)/Blackfin/include/cycle_count_bf.h $(VDSP)/Blackfin/include/fract.h $(VDSP)/Blackfin/include/fract2float_conv.h 
	@echo ".\main.c"
	$(VDSP)/ccblkfn.exe -c .\main.c -file-attr ProjectName=LMS2 -g -structs-do-not-overlap -no-multiline -D DO_CYCLE_COUNTS -double-size-32 -decls-strong -warn-protos -proc ADSP-BF533 -o .\Debug\main.doj -MM

./Debug/LMS2.dxe :$(VDSP)/Blackfin/ldf/adsp-BF533.ldf $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtsf532y.doj ./Debug/lms_process.doj ./Debug/main.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/__initsbsz532.doj $(VDSP)/Blackfin/lib/cplbtab533.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/crtn532y.doj $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsmall532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libc532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/librt_fileio532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libevent532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libcpp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libf64ieee532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libdsp532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libsftflt532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libetsi532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libssl532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libdrv532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/Debug/libusb532y.dlb $(VDSP)/Blackfin/lib/bf532_rev_0.5/libprofile532y.dlb 
	@echo "Linking..."
	$(VDSP)/ccblkfn.exe .\Debug\lms_process.doj .\Debug\main.doj -L .\Debug -add-debug-libpaths -flags-link -od,.\Debug -o .\Debug\LMS2.dxe -proc ADSP-BF533 -MM

endif

ifeq ($(MAKECMDGOALS),LMS2_Debug_clean)

LMS2_Debug_clean:
	-$(RM) "Debug\lms_process.doj"
	-$(RM) "Debug\main.doj"
	-$(RM) ".\Debug\LMS2.dxe"
	-$(RM) ".\Debug\*.ipa"
	-$(RM) ".\Debug\*.opa"
	-$(RM) ".\Debug\*.ti"
	-$(RM) ".\Debug\*.pgi"
	-$(RM) ".\*.rbld"

endif


