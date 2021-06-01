def mad_berechnen (syst,diast):

    """Berechnet den mittleren arteriellen Blutdruck (MAD)
    auf Basis der Parameter syst [mmHg] und diast [mmHg]. 
    
    :param syst: systolischer Blutdruckwert in mmHg
    :param diast: diastolischer Blutdruckwert in mmHg
    
    Beispiel: 
    >>> mad_berechnen(130,80)
    105"""
    
  # Berechnung MAD
    mad = diast+(0.5*(syst-diast))
  # Runden auf ganze Zahlen
    return int(round(mad,0))