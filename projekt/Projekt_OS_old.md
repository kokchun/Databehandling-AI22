# Projekt OS

<img src="os_rings.svg" alt="OS rings" width="100"/>

**Syftet** med det här projektet är att använda verktygen ni lärt er i **Pandas**, **Matplotlib**, **Seaborn** för att rensa och filtrera ut användbar information och visualisera den på ett enkelt sätt. 

I den här projektet ska ni hämta historisk data på OS från [Kaggle][OS_data] för att göra dataanalys. Ni ska jobba i grupper på 2-3 personer. 

[OS_data]: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

## Uppgift 0 - Uppvärmning

Börja med att göra explorativ dataanalys över hela datasettet för att bekanta er med datan. Exempel:

```py
df.head()
df.describe()
df.info()
df.index
df.columns
```

Generella frågor att besvara med hjälp av datan: 
1. hur många länder som är med i datan?
2. vilka länder är med? (förkortningarna räcker)
3. vilka sporter är med?
4. vilka medaljtyper finns det?
5. ta reda på statistik för åldern medelvärde, median, min, max, standardavvikelse, 
6. utforska datan vidare med egna frågor

Se även till att plotta några intressanta features, exempelvis:

1. histogram över åldrar
2. cirkeldiagram över könsfördelningen
3. stapeldiagram över topp 10 länder som tagit flest medaljer 
4. plotta gärna fler saker som är intressant.

## Uppgift 1 - Landstatistik

Ni får ett land tilldelat till er grupp. Börja med att **anonymisera** kolumnen med idrottarnas namn med hashfunktionen SHA-256.

 Undersök därefter hur det gått för landet i OS genom tiderna. Visualisera exempelvis:
- de sporter de fått flest medaljer i 
- antal medaljer per OS

Skapa fler plots för att visualisera flera aspekter kring ert land. 

### Bonus  
Välj ytterligare något land ni vill jämföra med och använd lämpliga visualiseringar för att göra jämförelser. 

## Uppgift 2 - Sportstatistik

Välj 2-4 sporter och skapa lämpliga grafer/diagram för att visualisera exempelvis: 
- medaljfördelning mellan länder i sporterna
- åldersfördelning i sporterna

Skapa fler plots för att visualisera olika aspekter kring sporterna. Gör gärna subplots för att jämföra sporterna mot varandra. 

## Uppgift 3 - Presentation

Skapa en snygg presentation i en Jupyter notebook för uppgift 1 och uppgift 2 med både kod och markdown. Utforska gärna på egen hand plotly och framförallt plotly.express för snygga och enkla visualiseringar.

Presentera därefter i grupp på ca 10-15 min/grupp där ni bland annat förklarar: 
- vilka frågeställningar har ni haft.
- hur ni gått tillväga för att besvara dessa frågeställningar.
- varför ni valt just de olika diagrammen/graferna

Notera att **alla** i gruppen ska presentera.

## Bedömning

Om ni har fått någon kodsnutt från någon annan eller hittat i någon sida är det **viktigt** att ni källhänvisar, annars räknas det som plagiat. Skriv en kommentar bredvid koden som ni har tagit.   

### Godkänt

- löst uppgift 0-3 på ett korrekt sätt 
- koden är kommenterad med relevanta kommentarer
- variabelnamnen är bra valda 
- gjort flera relevanta git commits
- presentationen är tydlig och lättförståelig

### Väl Godkänt

Uppfyllt allt för godkänt samt:
- koden är effektiv och enkel att följa
- koden är välstrukturerad med lämpliga funktioner
- kommentarerna är datavetenskapligt korrekta
- gjort samtliga uppgifter
- graferna är snygga, tydliga och välvalda med bra motivation