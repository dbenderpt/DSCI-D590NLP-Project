

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

#test articles
articles = {
    "period1": [
        "Stock market hits record high despite economic concerns.",
        "Investors are optimistic about upcoming earnings season.",
        "New policies are expected to boost the economy.",
        "Corporate profits exceed analysts' expectations.",
        "Trade negotiations show signs of progress.",
        "Healthcare sector stocks rally on positive trial results.",
        "Manufacturing sector sees unexpected growth in Q4.",
        "Auto industry rebounds as supply chain issues ease.",
        "Consumer spending hits decade-high levels.",
        "Major airline reports record-breaking quarterly revenue.",
        "Renewable energy stocks surge on new government incentives.",
        "E-commerce giant expands into new international markets.",
        "Tech innovation drives productivity gains in multiple sectors.",
        "Green technology firm reports exponential growth in adoption.",
        "Major financial institution announces increased dividend payouts.",
        "New startup receives substantial venture capital funding.",
        "Job market reports show highest employment rate in two decades.",
        "Luxury goods sector experiences rapid global sales growth.",
        "Pharmaceutical breakthrough expected to save millions of lives.",
        "Electric vehicle adoption hits record high, boosting auto industry.",
        "Global tourism sees strong rebound after years of stagnation."
    ], #q1
    "period2":[
        "Stock market achieves all-time highs despite headwinds.",
        "Earnings season kicks off with strong corporate profits.",
        "Government announces substantial infrastructure investments.",
        "Tech startups report significant venture capital funding rounds.",
        "Green energy sector surges amid favorable policies.",
        "Consumer confidence climbs to decade highs.",
        "Healthcare innovation receives global accolades.",
        "Auto sector rebounds on easing supply chain issues.",
        "Global markets stabilize as inflation fears abate.",
        "E-commerce leader expands into new growth markets.",
        "Pharma breakthrough promises to revolutionize treatment.",
        "Airline industry sees surge in bookings post-recovery.",
        "Housing market shows resilience amid economic concerns.",
        "Cryptocurrency adoption surges in emerging markets.",
        "Job creation hits a record-breaking pace.",
        "Luxury sector posts extraordinary growth in demand.",
        "Tech innovation leads to massive productivity gains.",
        "Energy sector booms with renewable initiatives.",
        "Retail sales surge ahead of holiday season.",
        "Tech giant faces antitrust investigations.",
        "Major supply chain disruptions hinder global recovery.",
        "Oil prices drop amidst lackluster demand projections.",
        "Retail chain struggles with declining foot traffic.",
        "Inflation fears spark concerns across sectors."
    ], #q2
    "period3":[
        "Tech stocks show recovery after sharp declines.",
        "Housing market stabilizes following months of turbulence.",
        "Healthcare advances create optimism in the sector.",
        "Manufacturing growth falters amidst supply chain issues.",
        "Consumer confidence dips slightly in latest reports.",
        "Tech innovation continues to attract strong investment.",
        "Energy sector faces challenges as demand fluctuates.",
        "Global markets rally on easing geopolitical tensions.",
        "Retail sales grow despite broader economic concerns.",
        "Oil prices surge as OPEC adjusts output targets.",
        "Airline industry faces mixed outcomes from travel policies.",
        "Renewable energy adoption accelerates in key markets.",
        "Major IPO sees solid opening despite investor caution.",
        "E-commerce leader under scrutiny for business practices.",
        "Financial sector posts mixed results amid rising rates.",
        "Pharma sector achieves milestone in research.",
        "Cryptocurrency markets stabilize after prolonged volatility.",
        "Consumer spending rebounds in time for holiday season.",
        "Luxury goods see renewed interest in global markets.",
        "Tech layoffs impact hiring trends in Silicon Valley."
    ], #q3
    "period4": [
        "Global markets rally on strong earnings reports.",
        "Consumer spending growth moderates amid inflation fears.",
        "Tech firms report mixed earnings as challenges persist.",
        "Healthcare advances receive regulatory approval.",
        "Energy sector faces renewed pressure on sustainability targets.",
        "Luxury goods sales falter in key international markets.",
        "Cryptocurrency adoption gains traction despite risks.",
        "Retail sector posts stronger-than-expected quarterly results.",
        "Airline bookings rise as restrictions ease globally.",
        "Pharma innovation promises breakthrough treatments.",
        "Manufacturing output remains subdued despite policy support.",
        "Green technology investments continue to soar globally.",
        "Housing market challenges buyers amidst limited supply.",
        "Oil market remains volatile as supply-demand dynamics shift.",
        "Auto sector sees mixed recovery trends regionally.",
        "E-commerce leader launches major new product line.",
        "Financial sector gains on strong quarterly performances.",
        "Consumer confidence rebounds in key markets.",
        "Tech regulation concerns weigh on broader sector performance.",
        "Renewable energy projects advance on global scale."
    ] #q4
}

#test market data
marketResults = {
    "period1": [ 0.00693749,  0.02417518, -0.00085423,  0.01359724, -0.00395965,  0.01378757,  0.00545421,  0.00601496,  0.00317609,  0.01406262,  0.00794821,  0.00953494,  0.01005687,  0.01867683, -0.0015102 ,  0.00116904,  0.00212728,  0.00075445,  0.02246813,  0.00356736,  0.00431695,  0.0045158 ,  0.00307257,  0.0105453 , -0.01937916,  0.00780296, -0.00562809, -0.00459847,  0.00158593,  0.00299259,  0.00194083,  0.00140079, -0.00430508,  0.00235822,  0.01551212, -0.0048419 , -0.00791639,  0.01538617,  0.01121197,  0.00965668,  0.005467  ,  0.018695  ,  0.00880858, -0.00380928,  0.02104497, -0.00442736,  0.01157639,  0.00520356,  0.00965723,  0.0103038 ,  0.00625115,  0.00195907, -0.00611572, -0.00950488,  0.01160703,  0.00670691, -0.00555366, -0.00723138, -0.00417231,  0.00371193,  0.01904331,  0.01233295,  0.01653794], #q2
    "period2": [-0.00883504, -0.01142346, -0.00273958, -0.00119106,  0.00342153,  0.00941131, -0.00578967, -0.02066617, -0.02617691, -0.00497789, -0.00733949, -0.00951142, -0.01787613, -0.02477337, -0.00279397, -0.0216669 , -0.01197819, -0.02530239, -0.00433388, -0.01200166, -0.01541435,  0.00484413, -0.03155591, -0.0106742 , -0.01874003, -0.01119853, -0.00123872, -0.01110171, -0.01319534, -0.01529281, -0.00462205,  0.00805132, -0.01275852, -0.01967347, -0.01191446, -0.00341336, -0.02614739, -0.01214277, -0.00712246, -0.0140942 , -0.02408309, -0.02267136, -0.02789461, -0.017528  , -0.01256221, -0.01096728, -0.00507036, -0.01518837, -0.02424687,  0.00535391, -0.00586467, -0.01859633,  0.00383601, -0.03500535, -0.01100697, -0.03224646, -0.0078745 , -0.03374861, -0.00000344,  0.00856766, -0.01690637, -0.00760732, -0.00997732], #q3
    "period3": [0.00422766, 0.00359997, 0.0036717, 0.00370432, 0.00445071, 0.00384243, 0.0041078, 0.0038592, 0.00408961, 0.00394958, 0.00393149, 0.00402023, 0.00367258, 0.00423157, 0.00427987, 0.00387172, 0.00360845, 0.00415048, 0.00366579, 0.00425885, 0.00412226, 0.00455351, 0.0037351, 0.00344744, 0.00340987, 0.00400393, 0.0040394, 0.00357122, 0.00464863, 0.00401952, 0.00412224, 0.00400982, 0.00387381, 0.00454885, 0.00404404, 0.00388131, 0.00417453, 0.00409057, 0.00412929, 0.00404048, 0.00369204, 0.00377211, 0.00376365, 0.00382796, 0.00443702, 0.0040047, 0.00424966, 0.00461991, 0.00402273, 0.00364884, 0.00411447, 0.00411024, 0.0041808, 0.00399654, 0.00441266, 0.00456488, 0.0039313, 0.00408922, 0.00442097, 0.00357309, 0.00420481, 0.00459891, 0.00403146], #q4
    "period4": [-0.5273189130458702, 0.2974859306792971, -0.0346624586423875, -0.7175624845882792, 0.1839048591581951, 0.6960304931633325, -0.2142592496403462, 0.8842614550582668,-0.2017983601266151, 0.1232823245032849, 0.4358312185154974, 0.7790619920287023,-0.6718660899813549, -0.6823461684591365, 0.3471519648402647, -0.7225778365104344,0.8488656797540801, 0.5263811777475514, -0.3155206656246992, -0.9734130621243549,0.0558669074207328, 0.9369920403650994, 0.1608812928322776, 0.1630227849525587,0.8987076626376505, -0.5949391853229039, -0.8956280245930424, 0.5626858090211235,0.2641579673286535, -0.6112549569509227, -0.8392944630571914, 0.9502644631341866,-0.2983514997666993, 0.6549672689936537, -0.6170244590407851, 0.3158664380760677,-0.1157268507282887, -0.6627270084983079, 0.7566119477438015, 0.3508000730361027,0.4141425131054245, -0.3214601143101857, -0.7121319295137541, 0.4062199075242472,0.4415664198741144, -0.8652095597814298, -0.4759228262844657, -0.8481097283435669,0.0870082928998784, -0.1206627220707263, 0.0567540527234464, 0.3884461891113944,0.8892114280543629, -0.7540202393740788, -0.3062546501969507, 0.0384361178272109, 0.7038206361983282, 0.6946121673009448, -0.4150648716467979, 0.7595421956750048, -0.2477612562382461, -0.2342863239709546, 0.0133276352193599, 0.7001736812292613] #y2q1
}

def analyzeSentiment(article):
    x = TextBlob(article)
    return x.sentiment.polarity

def analyzePeriod(periodCall):
    periodArticles = articles[periodCall]
    totalSentiment = 0
    for i in range(len(periodArticles)):
        x = analyzeSentiment(periodArticles[i])
        # print(x)
        totalSentiment = totalSentiment + x
    return totalSentiment/len(periodArticles)

def getQuarterPerformance(periodCall):
    periodPerformance = marketResults[periodCall]
    totalGrowth = 0
    for i in range(len(periodPerformance)):
        totalGrowth = totalGrowth + periodPerformance[i]
    return totalGrowth


data = {
    'sentimentAnalyses': [analyzePeriod("period1"),analyzePeriod("period2"),analyzePeriod("period3"),analyzePeriod("period4")],
    'stockPerformance': [getQuarterPerformance("period1"),getQuarterPerformance("period2"),getQuarterPerformance("period3"),getQuarterPerformance("period4")]
}

df = pd.DataFrame(data)
print(df)


correlation = df["sentimentAnalyses"].corr(df["stockPerformance"])
print(correlation)

plt.figure(figsize=(8, 6))
plt.scatter(df["sentimentAnalyses"], df["stockPerformance"], alpha=0.6, color='blue')
plt.title(f"Sentiment Analysis vs Stock Performance\nCorrelation: {correlation:.2f}")
plt.xlabel("Sentiment Score (Positivity)")
plt.ylabel("Stock Performance (Growth)")
plt.show()