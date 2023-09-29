from generate import Generate
from uniformity import Uniformity
from independence import Independence
import numpy
prueba = Generate(5,8,1280,63)
valores = prueba.congruentLinearGenerator(100)
lista4 = [0.00115,0.22461,0.48433,0.09089,0.68942,
        0.33142	,0.4653,	0.51518,	0.02395,	0.66448,
        0.00066,	0.45972,	0.84643,	0.79442,	0.97112,
        0.2227826,	0.88826,	0.62199,	0.00492,	0.08876,
        0.25956,	0.79147,	0.38179,	0.73897,	0.7936,
        0.23954,	0.68597,	0.44053,	0.01575,	0.91632,
        0.07777,	0.29237,	0.78409,	0.90845,	0.17047,
        0.6064,	0.78343,	0.8886,	0.31993,	0.61788,
        0.69844,	0.81772,	0.17588,	0.7603,	0.9388,
        0.63905,	0.52108,	0.20263,	0.31928,	0.59803
    ]


poker = Independence(lista4)
poker.poker(3)


