import yfinance as yf
import matplotlib.pyplot as plt
import os
import warnings


TEMP_IMAGE_DIR = "temp_images"


os.makedirs(TEMP_IMAGE_DIR, exist_ok=True)
warnings.simplefilter(action='ignore', category=FutureWarning)


def graph(ticker):
    msft = yf.Ticker(ticker)
    hist = msft.history(period="max")
    
    plt.figure(figsize=(10, 6))
    plt.plot(hist.index, hist['Close'], label='Close Price', color='red')
    plt.title(f'{ticker} Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid(True)

    image_path = os.path.join(TEMP_IMAGE_DIR, f'{ticker}_stock_price.png')
    plt.savefig(image_path)
    plt.close()

    return image_path




def get_recommendations_summary(ticker):
    msft = yf.Ticker(ticker)
    
    # Get recommendations summary
    recommendations_df = msft.recommendations_summary

    formatted_data = "Recommendations Summary for {}: \n\n".format(ticker)
    formatted_data += recommendations_df.to_markdown(index=False)

    return formatted_data



def news(ticker):
    msft = yf.Ticker(ticker)
    hist = msft.history(period="1mo")
    news_data = msft.news
    i=0
    articles=[]
    for article in news_data:
        if i>=2:
            break
        title = article['title']
        link = article['link']
        articles.append(f" {title}\n\n {link}\n\n")
        i+=1
    return "\n".join(articles)




