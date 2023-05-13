from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from ai_model_resource.api import SuggestModel
import pandas as pd


class SimilarRecipe:

    """
    Class SimilarRecipe()
        A class that finds similar healthy recipes based on keywords.

        Attributes:
        -----------
        df : pd.DataFrame
            A Pandas DataFrame that contains healthy recipe data.

        Methods:
        --------
        combFeatures(row):
            Combines the title and keywords columns of a DataFrame row.

        getTitle(index):
            Returns the title of a recipe based on its index.

        getDescription(index):
            Returns the description of a recipe based on its index.

        getSimilarRecipes(keywords):
            Finds similar healthy recipes based on the given keywords and returns a dictionary containing 
            the top 5 matching recipes along with their titles, descriptions, and images.
    """

    def __init__(self) -> None:
        self.df = pd.read_csv('healthy_recipes.csv')


    def combFeatures(self,row):
        return row["title"] + " " + row["keywords"]


    def getTitle(self,index):
        return self.df[self.df.index == index]["title"].values[0]


    def getDescription(self,index):
        return self.df[self.df.index == index]["description"].values[0]
    

    def getSimilarRecipes(self, keywords):
        output = []
        result = False

        self.df["combinedFeatures"] = self.df.apply(self.combFeatures,axis=1)
        
        cv = CountVectorizer()
        countMatrix = cv.fit_transform(self.df["combinedFeatures"])
        similarityMatrix = cosine_similarity(countMatrix)

        query = " ".join(keywords)
        queryMatrix = cv.transform([query])

        similarity_scores = list(enumerate(cosine_similarity(queryMatrix, countMatrix)[0]))
        sorted_similar = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]
        top_5 = sorted_similar[:5]

        for index,score in top_5:
            title = self.getTitle(index)
            b64_image = SuggestModel().generate_image(title)
            description = self.getDescription(index)
            meal = {'title': title, 'description': description, 'image': b64_image}
            output.append(meal)
            result = True
            
        return {'meals': output},result
