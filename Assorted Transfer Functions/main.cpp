//  Localization (Independent of Detection)
//  main.cpp
//  Created by Jacob Violette on 11/25/16.
//  Copyright © 2016 Jacob Violette. All rights reserved.
//
#include <iostream>
#include <cmath>
#include <math.h>
#include <iomanip>

int main()  {
//  Needed inputs
    double Lat=29.1846166785476*M_PI/180; //Radians
    double Long=-81.1261695007229*M_PI/180;  //Radians
    double Alt=100;  //Meters
    double Yaw=0*M_PI/180; //Positive Heading CW from North (Radians)
    double XPix=2448; //Number of pixels in X direction
    double YPix=2048; //Number of pixels in the Y direction
    double TargetR=1; //Row that the target is in
    double TargetC=2448; //Column that the target is in
    double XFOV=19.17*M_PI/180; //Radians
    double YFOV=16.09*M_PI/180; //Radians
    double REarth=6378137; //meters
    
//  Sightline Roll/Pitch Angles
    double Roll=((XPix/2)-TargetC)*(XFOV/XPix);
    double Pitch=((YPix/2)-TargetR)*(YFOV/YPix);
    
// Translation from plane
    double XTrans=-(cos(Pitch)*sin(Roll)*Alt)/(cos(Pitch)*cos(Roll));
    double YTrans=(sin(Pitch)*Alt)/(cos(Pitch)*cos(Roll)); //Place "-" in front of sin to invert Y direction if needed
    
//  Calculations
     double theta=atan2(XTrans,YTrans); //Positive target angled CW from heading
     double dist=sqrt(pow(XTrans,2)+pow(YTrans,2)); //Ground distance from plane to target
    // double latT=asin(sin(Lat)*cos(dist/REarth)+cos(Lat)*sin(dist/REarth)*cos(theta+Yaw))*180/M_PI;
    // double longT=(Long+atan2(sin(theta+Yaw)*sin(dist/REarth)*cos(Lat),cos(dist/REarth)-(sin(Lat)*sin(latT))))*180/M_PI;
    double east=cos(Yaw+theta)*dist;
    double north=sin(Yaw+theta)*dist;
    double latT=(Lat+(east/110574*M_PI/180))*180/M_PI;
    double longT=(Long+(north/111320/cos(Lat)*M_PI/180))*180/M_PI;
    std::cout << std::setprecision(15) << "Lat,Long: " <<latT<< "," <<longT<< "\n";
    std::cout << std::setprecision(8) << "XTrans,YTrans (meters): " <<XTrans<< ", " <<YTrans<< "\n";
    
    //Note that half X Swath is 16.886806 meters (+/- 2 cm.)
    //Note that half Y Swath is 14.334295 meters (+/- 2 cm.)
    
    //Note that top and bottom swath lines have a half swath variation of about 20 cm.
    //Note that left to right swath lines have a half swath variation that is very small (mm)
}

