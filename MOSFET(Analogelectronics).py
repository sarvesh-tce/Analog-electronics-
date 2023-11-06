VGG = float(input(" enter VGG : "));
ID = float(input(" enter ID in ampere : "));
RD = float(input(" enter RD : "));

# FOR DEPLETION TYPE MOSFET FIXED BIAS :

VGS = VGG ;
VDS = float(VDD - ( ID * RS ));

# FOR DEPLETION TYPE MOSFET VOLTAGE DIVIDER BIAS :

R1 = float(input(" enter R1 : "));
R2 = float(input(" enter R2 : "));
RS = float(input(" enter RS : "));
IS = float(input(" enter IS in ampere : "));

VG = float(((R2 / ( R1 + R2 )) * VDD));
VGS = float(( VG - ( IS * RS )));
VDS = float((VDD -(ID * ( RD + RS ))));

# DISPLAYMENT :

print = (" \n MOSFET FIXED BIAS " );
print = (" VGS = " , VGS , " V ");
print = (" VDS = " , VDS , " V ");

print = (" \n VOLTAGE DIVIDER BIAS " );
print = (" VGS = " , VGS , " V ");
print = (" VDS = " , VDS , " V ");
print = (" VG = " , VG , " V ");