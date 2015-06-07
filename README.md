# hvembliverstatsminister

Dette projekt indsamler data fra danske bookmakers og udregner herudfra den implicitte betingede sandsynlighed for at Helle Thorning og Lars Løkke, respektive, bliver statsminister efter valget. Sandsynligheden er betinget på at en af de to kandidater
bliver statsminister.

data.csv indeholder det indsamlede data med flg. variable:
date: dato for indsamling i MMDD format
time: tidspunkt for indsamling i TTMM format, 
bf_llr: Betfairs odds for LLR
bf_hts: Betfairs odds for HTS
ds_llr: Danske Spils odds for LLR
ds_hts: Danske Spils odds for HTS
ub_llr: Unibets odds for LLR
ub_hts: Unibets odds for HTS
nb_llr: Nordicbets odds for LLR
nb_hts:Nordicbets odds for HTS

fv15bets.py indsamler data, opdaterer csv filen og danner grafer.

danfigurer.py danner figurer uden at indsamle data.

Spørgsmål kan skrives her eller rettes til @hhsievertsen og @njharbo.

God fornøjelse.
