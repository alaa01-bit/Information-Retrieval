
import re

class SentimentAnalyzer:
    POSITIVE_WORDS = {
        "good", "great", "excellent", "amazing", "awesome", "fantastic", "delicious", "yummy", "tasty",
        "love", "loved", "best", "wonderful", "nice", "pleasant", "friendly", "superb", "perfect",
        "courteous", "liked", "beautiful", "classy", "recommend", "must try", "enjoyed", "impressive"
    }

    NEGATIVE_WORDS = {
        "bad", "worst", "terrible", "horrible", "awful", "disgusting", "pathetic", "hate", "hated",
        "disappointed", "poor", "slow", "rude", "dirty", "unhygienic", "stale", "tasteless", "average",
        "expensive", "mess", "sick", "poisoning", "avoid", "waste", "horrendous", "hopeless"
    }

    @staticmethod
    def analyze(text):
        if not text or not text.strip():
            return 0.5

        lower_text = text.lower()
        words = re.split(r'\W+', lower_text)

        pos_count = 0
        neg_count = 0

        for word in words:
            if word in SentimentAnalyzer.POSITIVE_WORDS:
                pos_count += 1
            if word in SentimentAnalyzer.NEGATIVE_WORDS:
                neg_count += 1

        total_emotional_words = pos_count + neg_count
        if total_emotional_words == 0:
            return 0.5
        
        return float(pos_count) / total_emotional_words
