VCC = float(intput("enter VCC in volts :"));
VBB = float(intput("enter VBB in volts :"));
VBE = float(intput("enter VBE in volts :"));
RB = float(input("enter RB :"));
RC = float(input("enter RC :"));
RE = float(input("enter RE :"));
BETA = float(input("enter the current gain ( BETA ) in the circuit :"));

# FOR FIXED BIAS CONFIGURATION :

IB = float(( VBB - VBE ) / RB ) ; 
IC = float( BETA * IB );
VCE = float( VCC - ( IC * RC ));
IE = float(( BETA + 1 ) * IB );

# FOR EMITTER BIAS CONFIGURATION :

IB = float(( VBB - VBE ) / ( RB + ( ( BETA + 1 ) * RE ) ) ) ; 
IC = float( BETA * IB ); 
VCE = float( VCC - ( IC * ( RC + RE )));
IE = float(( BETA + 1 ) * IB );

# FOR VOLTAGE DIVIDER BIAS CONFIGURATION :

R1 = float(input("enter R1 : "));
R2 = float(input("enter R2 : "));
VTH = float(( R2 / ( R1 +R2 )) * VCC );
RTH = float(( R1 * R2 ) / ( R1 + R2 ));

IB = float((( VTH - VBE ) / ( RTH + ( BETA + 1 ) * RE )));
IC = float( BETA * IB ); 
VCE = float( VCC - ( IC * ( RC + RE )));
IE = float(( BETA + 1 ) * IB );

# FOR COLLECTOR FEEDBACK CONFIGURATION :

RF = float(input(" enter RF "));

IB = float((( VBB - VBE ) / ( RF + ( BETA * ( RC + RE ))))) ;
IC = float( BETA * IB ); 
VCE = float( VCC - ( IC * ( RC + RE )));
IE = float(( BETA + 1 ) * IB );

# RESULT DISPLAY :

print( " \n FIXED BIAS CONFIGURATION " )
print( " IB = " , IB , " A " );
print( " IC = " , IC , " A " );
print( " VCE = " , VCE , " V " );
print( " IE = " , IE , " A " );

print( " \n EMITTER BIAS CONFIGURATION " )
print( " IB = " , IB , " A " );
print( " IC = " , IC , " A " );
print( " VCE = " , VCE , " V " );
print( " IE = " , IE , " A " );

print( " \n VOLTAGE DIVIDER BIAS CONFIGURATION " )
print( " IB = " , IB , " A " );
print( " IC = " , IC , " A " );
print( " VCE = " , VCE , " V " );
print( " IE = " , IE , " A " );

print( " \n COLLECTOR FEEDBACK CONFIGURATION " )
print( " IB = " , IB , " A " );
print( " IC = " , IC , " A " );
print( " VCE = " , VCE , " V " );
print( " IE = " , IE , " A " );