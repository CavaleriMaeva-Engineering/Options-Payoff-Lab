import numpy as np 
from .base import Option

class AsianOption(Option) :
    """
    Cette classe implémente le calcul du payoff pour une option asiatique (path-dependent).
    
    À la différence des options européennes classiques, le gain d'une option asiatique 
    dépend de la moyenne des prix de l'actif sous-jacent observés durant toute la durée 
    de vie de l'option, plutôt que du seul prix à l'échéance.
    
    Cette approche permet de lisser la volatilité et de réduire le risque de manipulation 
    du cours du sous-jacent à la date de clôture.
    """
    
    def __init__(self,strike,expiry,premium=0.0,is_call=True,average_type='arithmetic') :
        super().__init__(strike,expiry,premium)
        self.is_call=is_call
        self.average_type=average_type
        
    
    def payoff(self,spot) :
        """
        Calcule le payoff de l'option asiatique en fonction de la moyenne 
        du chemin des prix (Path-Dependent).
        """
       #Calcul de la valeur de référence (moyenne des prix observés)
        if self.average_type=='arithmetic' :
            moyenne=np.mean(spot)
        elif self.average_type=='geometric' :
            moyenne=np.exp(np.mean(np.log(spot)))
        #Calcul du gain final selon la direction du contrat (Call ou Put)
        if self.is_call :
            return np.maximum(0,moyenne-self.K)
        else :
            return np.maximum(0,self.K-moyenne)
        
class BarrierOption(Option) :
    """
    Cette classe implémente le calcul du payoff pour une option à barrière (path-dependent).
    L'activation (Knock-in) ou la désactivation (Knock-out) du contrat dépend du franchissement 
    d'un seuil de prix (H) durant la période de détention.
    """
    
    def __init__(self,strike,expiry,barrier,premium=0.0,is_call=True,is_knock_in=True,is_up=True) :
        super().__init__(strike,expiry,premium)
        self.is_call=is_call
        self.barrier=barrier
        self.is_knock_in=is_knock_in
        self.is_up=is_up
        
    def payoff(self,spot) :
        #Détermine si la barrière a été franchie
        if self.is_up :
            has_hit_barrier=np.max(spot)>=self.barrier
        else :
            has_hit_barrier=np.min(spot)<=self.barrier
            
        #Détermine si l'option est vivante 
        #Si knock_in seulement si la barrière est franchie
        #Si knock_out seulement si la barrière n'est pas franchie
        if self.is_knock_in :
            is_active=has_hit_barrier
        else :
            is_active=not has_hit_barrier
        
        #Calcul du payoff 
        if is_active :
            if self.is_call :
                return np.maximum(0,spot[-1]-self.K)
            else :
                return np.maximum(0,self.K-spot[-1])
        else :
            return 0.0
            
            
class LookBackOption(Option) :
    """
    Cette classe implémente l'option Lookback (path-dependent).
    Elle permet de réduire le risque de timing en utilisant les prix extrêmes 
    (maximum ou minimum) atteints par l'actif durant la période.
    
    Types supportés :
    - 'Fixe' : On compare un extrême au Strike K.
    - 'Flottant' : Le Strike est remplacé par l'extrême atteint.
    """
    
    def __init__(self,strike,expiry,premium=0.0,is_call=True,type_option='Flottant') :
        super().__init__(strike,expiry,premium)
        self.is_call=is_call
        self.type_option=type_option

    def payoff(self,spot) :
        if self.type_option=='Fixe' :
            if self.is_call :
                return np.maximum(0,np.max(spot)-self.K)
            else :
                return np.maximum(0,self.K-np.min(spot))
        elif self.type_option=='Flottant' :
            if self.is_call :
                return spot[-1]-np.min(spot)
            else :
                return np.max(spot)-spot[-1]
        
            
            
            
    
        
        
        
        
        
        
        
