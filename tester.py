import goslate
t = 'Une aura de bien-être fait récupérer la moitié de ses PV max à la cible.'
gs = goslate.Goslate()
f = gs.translate(t, 'en')
print(f)
