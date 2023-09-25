PROC IMPORT OUT= WORK.transport                                                                                                           
            DATAFILE= "C:\Users\dsauvetre\Desktop\Transport.xls.xls"                        
            DBMS=xls REPLACE;                                                                                                     
     GETNAMES=YES;                                                                                                                      
RUN; 

/* MODELES A CHOIX BINAIRE */

proc contents;	
title 'Contenu du fichier TRANSPORT.XLS';
run;
proc print data=transport;
run;
proc means; 	/* statistiques descriptives */					
title 'Statistiques descriptives';
run;





/* S1 : Le modèle de probabilité linéaire i.e. OLS  */

proc reg data=transport;
model y=x/clb hcc hccmethod=1;	* utilisation robuste se; 	
title 'OLS avec robuste se';
output out=olsout p=probaols; 				
run;

proc print data=olsout; 			
title 'Prévisions avec le modèle de probabilité linéaire (OLS)';
run;

/* On obtient des probabilités négatives et d'autres supérieure à 1 */




/* S2: le modèle  PROBIT  */

proc qlim data=transport outest=estim method=QUANEW;			/* qlim = qualitative limite */
model y =x/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit';
run;

/* si ne converge pas on change la methode: */
/*METHOD=CONGRA DBLDOG NMSIMP NEWRAP NRRIDG QUANEW TRUREG*/

proc print data=probitout (obs=21); 
title 'Sortie du probit';
run;
/* Meff = marginal effect */ 

/*  Calculs des valeurs prédites  */
data transport2;
set probitout;
pnormale = probnorm(xbeta_y);  * calcul des probabilités loi normale;
phat = (pnormale >= .5); 		 * phat = 1 si p >= .5;
run;
proc print data=transport2;
run;
/* on compare y = ^y */

/* Graphique pour comparer prev par OLS et prev par PROBIT */
* Pour ne garder que certaines variables;

/* le fichier des ols et celui de probit: */
DATA NEW22;
SET olsout(keep=probaols);
RUN;
DATA NEW23;
SET transport2(keep=pnormale);
RUN;
/* concatenation des deux fichiers: */
DATA NEW2223;
MERGE new22 new23;
time=_n_; 
run;
/* graphique: */
proc gplot data=new2223;	
PLOT (pnormale probaols)*time/overlay legend=legend1 vref=1 vref=0;
SYMBOL interpol=join; 
 TITLE color=RED height=2 font=times "Comparaison de probabilité OLS vs PROBIT";                                                   
		LEGEND1 value=(tick=1 'prev Probit' tick=2 'Prev OLS') label=none;                                                         
run;

/* Calcul des effets marginaux à certains points : .5-1-1.5-2-2.5-3-3.5 */

PROC PRINT data=estim;
run;
/* nettoyage du fichier: */
data new;
set estim;
t=_n_;
if t=2 then delete;
drop _name_ _type_ _status_;
run;
proc print data=new;
run;

DATA marginal;
SET new;
aug=1.5;  /*  changer la valeur */
phi=intercept+aug*x;
effetm=((1/sqrt(2*3.14159265358979))*exp(-0.5*phi**2))*x;   /* densité de la loi normale */
probadephi=CDF('NORMAL',phi); 
run;
PROC PRINT data=marginal;
title 'Effet marginal et probabilités pour probit';
RUN;
/* pour aug = 0.5 : l'effet marginal est de 0.119 et la probabilite de prendre la voiture est de 53% */
/* pour aug = 1 : l'effet marginal est de 0.116 et la probabilite de prendre la voiture est de 59% */
/* pour aug = 1.5 : l'effet marginal est de 0.111 et la probabilite de prendre la voiture est de 65% */
/* ... */
/* effet marginal : une augmentation de l'attente du bus d'1 minute augmente la probabilite de prendre la voiture de 0.11 */







DATA nouveau;
set transport;
difference = (bustime - autotime)/5;
run;
PROC PRINT data=nouveau;
title 'tableau difference';
RUN;

proc qlim data=nouveau outest=estim method=QUANEW;			/* qlim = qualitative limite */
model y =difference/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit';
run;
proc print data=probitout (obs=21); 
title 'Sortie du probit';
run;

data nouveau;
set probitout;
pnormale = probnorm(xbeta_y);  * calcul des probabilités loi normale;
phat = (pnormale >= .5); 		 * phat = 1 si p >= .5;
run;
proc print data=nouveau;
run;


/* nettoyage du fichier: */
data nouveau2;
set estim;
t=_n_;
if t=2 then delete;
drop _name_ _type_ _status_;
run;
proc print data=nouveau2;
run;

DATA marginal2;
SET nouveau2;
aug=0.5;  /*  changer la valeur */
phi=intercept+aug*difference;
effetm=((1/sqrt(2*3.14159265358979))*exp(-0.5*phi**2))*difference;   /* densité de la loi normale */
probadephi=CDF('NORMAL',phi); 
run;
PROC PRINT data=marginal2;
title 'Effet marginal et probabilités pour probit';
RUN;



/* S3: le modèle  LOGIT  */

proc qlim data=transport;
model y=x/discrete(d=logit);
output out=logitout xbeta marginal; 
title 'Estimations logit';	
run;
proc print data=logitout;
run;

/* Effet marginal moyen EMM*/
proc means data=logitout;
var meff_p1_x meff_p2_x;
title 'Effet marginal moyen pour LOGIT';
run; 

/*  Calculs des Valeurs prédites  */
data transport3;
set logitout;
plogistic = CDF('LOGISTIC',xbeta_y,0,1); 		* calcul des probabilités;
phat = (plogistic >= .5); 				        * phat = 1 si p >= .5;
run;

proc print data=transport3;
var plogistic;
run;

DATA NEW33;
SET transport3(keep=plogistic);
RUN;

DATA NEW4;
MERGE new22 new23 new33;
time=_n_; 
run;

PROC PRINT data=new4;
RUN;

proc gplot data=new4;	
PLOT (pnormale probaols plogistic)*time/overlay legend=legend1 vref=1 vref=0;
SYMBOL interpol=join; 
 TITLE color=RED height=2 font=times "Comparaison de probabilité OLS vs PROBIT vs LOGIT";                                                   
		LEGEND1 value=(tick=1 'prev Probit' tick=2 'Prev OLS' tick=3 'Prev Logistic') label=none;                                                         
run;

/*XXXXXXXXXXXXXXXXX EN CHANGEANT Y=1 par Y=10 XXXXXXXXXXXXXXXXXXXXXXXXXX*/

DATA ESSAI10;
SET transport;
y10=y*10;
RUN;
PROC PRINT;
RUN;

/* S3: le modèle  PROBIT  */

proc qlim data=essai10 outest=estim method=QUANEW;			
model y10=x/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit s3';
run;

/*XXXXXXXXXXXXXXXXX EN CHANGEANT Y=1 par Y=1 et y=0 par 20 XXXXXXXXXXXXXXXXXXXXXXXXXX*/

DATA ESSAI12;
SET transport;
if y=0 then  y=20;
RUN;
PROC PRINT;
RUN;

/* S4: le modèle  PROBIT  */

proc qlim data=essai12 outest=estim method=QUANEW;			
model y=x/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit s4';
run;



/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX */
/* autres procedure POUR PROBIT: */
proc probit data=transport outest=estim;			
model y(event=last)=x; 			 
output out=probitout xbeta=xb ;
title 'Estimations Probit';
run;

proc probit data=transport outest=estim;			
model y(event=first)=x; 			 
output out=probitout xbeta=xb ;
title 'Estimations Probit';
run;
/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/
DATA ESSAInew;
SET transport;
y10=y+1;
if y10 =2 then y10=0;
RUN;
PROC PRINT;
RUN;

/* S3: le modèle  PROBIT  */

proc qlim data=essainew outest=estim method=QUANEW;			
model y10=x/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit s3';
run;
