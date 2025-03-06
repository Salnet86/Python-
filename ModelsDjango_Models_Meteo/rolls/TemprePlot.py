from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')  
import io
import matplotlib.pyplot as plt
import seaborn as sns




class TempPLT:
    @staticmethod
    def plotter(title, xlabel, ylabel, x, y):
        fig, ax = plt.subplots(figsize=(20, 5))
        sns.lineplot(x=x, y=y, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)
        return HttpResponse(img.getvalue(), content_type='image/png')
        

class BarPlot:
    @staticmethod
    def Barplotter(title, xlabel, ylabel, x, y):
        fig, ax = plt.subplots(figsize=(20, 5))
        sns.barplot(x=x, y=y, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)
        return HttpResponse(img.getvalue(), content_type='image/png')
        
