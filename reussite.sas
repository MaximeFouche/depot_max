PROC IMPORT OUT= WORK.REUSSITE                                                                                                          
            DATAFILE= "C:\Users\dsauvetre\Desktop\reussite.xls.xls"                        
            DBMS=xls REPLACE;                                                                                                     
     GETNAMES=YES;                                                                                                                      
RUN; 

/* MODELES A CHOIX BINAIRE */
/***************************/

/* statistiques descriptives */
proc contents;					
title 'Contenu du fichier REUSSITESAS.XLS';
run;
proc print data=REUSSITE;
run;
proc means; 						
title 'Statistiques de base';
run;
/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX */

/*XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX */
/* S1: le modèle  PROBIT  */

proc qlim data=reussite outest=estim method=QUANEW;			
model y = sexe meanbac baces bacs p4 p5 p6 p8/discrete; 			    * discrete pour probit;
output out=probitout xbeta marginal;
title 'Estimations Probit';
run;

/* si ne converge pas on change la methode: */
/*METHOD=CONGRA DBLDOG NMSIMP NEWRAP NRRIDG QUANEW TRUREG*/

proc print data=probitout (obs=114); 
title 'Sortie du probit';
run;
/* Meff = marginal effect */ 

/*  Calculs des valeurs prédites  */
data reussite2;
set probitout;
pnormale = probnorm(xbeta_y);  * calcul des probabilités loi normale;
phat = (pnormale >= .5); 		 * phat = 1 si p >= .5;
run;
proc print data=reussite2;
run;
/* on compare y = ^y */

/* Graphique pour comparer prev par OLS et prev par PROBIT */
* Pour ne garder que certaines variables;


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
aug=;  /* augmentation d'un point de la moyenne */
phi=intercept+aug*meanbac;
effetm=((1/sqrt(2*3.14159265358979))*exp(-0.5*phi**2))*meanbac;   /* densité de la loi normale */
probadephi=CDF('NORMAL',phi); 
run;
PROC PRINT data=marginal;
title 'Effet marginal et probabilités pour probit';
RUN;

DATA marginalbinaire;
SET new;
aug=1;  /* augmentation d'un point de la moyenne */
phi=intercept+aug*sexe;
effetm=((1/sqrt(2*3.14159265358979))*exp(-0.5*phi**2))*sexe;   /* densité de la loi normale */
probadephi=CDF('NORMAL',phi); 
run;
PROC PRINT data=marginalbinaire;
title 'Effet marginal et probabilités pour probit';
RUN;

DATA marginalbacs;
SET new;
aug=0;  /* augmentation d'un point de la moyenne */
phi=intercept+aug*bacs;
effetm=((1/sqrt(2*3.14159265358979))*exp(-0.5*phi**2))*bacs;   /* densité de la loi normale */
probadephi=CDF('NORMAL',phi); 
run;
PROC PRINT data=marginalbacs;
title 'Effet marginal et probabilités pour probit';
RUN;
