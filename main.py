import numpy as np
from core.vanilla import CallOption, PutOption
from matplotlib import pyplot as plt

def main():
  #Création des options
  mon_call=CallOption(100,1,5.0)
  mon_put=PutOption(100,1,5.0)

  #Scénarios de prix à l'échéance (S_T)
<<<<<<< HEAD
  prix_finaux=np.array([80, 90, 100, 110, 120])
=======
  S_T=np.array([80, 90, 100, 110, 120])
>>>>>>> b8ac6be4697328e157da429d2c817e149c68d6cc

  #Calcul des payoffs
  gains_call=mon_call.payoff(S_T)
  gains_put=mon_put.payoff(S_T)

  #Calcul des P&L
  pnl_call = mon_call.profit(S_T)
  pnl_put = mon_put.profit(S_T)
  
  #Affichage des résultats
  print(f"Prix du marché : {S_T}")
  print(f"Gains du Call  : {gains_call}")
  print(f"Gains du Put   : {gains_put}")
  
  #Visualisation
  plt.figure(figsize=(10, 6)) # Pour que le graphique soit grand
  plt.plot(S_T,pnl_call,label="P&L Call",color='blue')
  plt.plot(S_T,pnl_put,label="P&L Put",color='green')
  
  plt.axhline(0, color='black',linewidth=1.5)
  plt.axvline(mon_call.K,color='red',linestyle='--',alpha=0.5)
  
  plt.title("Profil de Profit et Perte (P&L) à l'échéance")
  plt.xlabel("Prix de l'action à l'échéance (S_T)")
  plt.ylabel("Profit / Perte net(te)")
  plt.grid(True,alpha=0.3) 
  plt.legend()
  plt.show()
  
if __name__=="__main__":
  main()
