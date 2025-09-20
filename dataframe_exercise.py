{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMhrg89FF8giWj/6tnSWySw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Udarbe-M/dataframe-exercise/blob/exercises/dataframe_exercise.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Creating a DataFrame\n",
        "\n",
        "import pandas as pd\n",
        "# Sample sales dataset (20 rows)\n",
        "data = {\n",
        "\"OrderID\": range(1001, 1021),\n",
        "\"Product\": [\n",
        "\"Laptop\", \"Mouse\", \"Keyboard\", \"Monitor\", \"Laptop\",\n",
        "\"Headphones\", \"Mouse\", \"Chair\", \"Desk\", \"Laptop\",\n",
        "\"Printer\", \"Keyboard\", \"Monitor\", \"Mouse\", \"Laptop\",\n",
        "\"Headphones\", \"Desk\", \"Monitor\", \"Printer\", \"Chair\"\n",
        "],\n",
        "\"Category\": [\n",
        "\"Electronics\", \"Accessories\", \"Accessories\", \"Electronics\", \"Electronics\",\n",
        "\"Accessories\", \"Accessories\", \"Furniture\", \"Furniture\", \"Electronics\",\n",
        "\"Electronics\", \"Accessories\", \"Electronics\", \"Accessories\", \"Electronics\",\n",
        "\"Accessories\", \"Furniture\", \"Electronics\", \"Electronics\", \"Furniture\"\n",
        "],\n",
        "\"Quantity\": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],\n",
        "\"Price\": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],\n",
        "\"Customer\": [\n",
        "\"Alice\", \"Bob\", \"Charlie\", \"Diana\", \"Ethan\",\n",
        "\"Fiona\", \"George\", \"Hannah\", \"Ian\", \"Jane\",\n",
        "\"Kyle\", \"Laura\", \"Mike\", \"Nina\", \"Oscar\",\n",
        "\"Paul\", \"Queen\", \"Robert\", \"Sarah\", \"Tom\"\n",
        "],\n",
        "\"Region\": [\n",
        "\"North\", \"South\", \"East\", \"West\", \"North\",\n",
        "\"South\", \"East\", \"West\", \"North\", \"South\",\n",
        "\"East\", \"West\", \"North\", \"South\", \"East\",\n",
        "\"West\", \"North\", \"South\", \"East\", \"West\"\n",
        "]\n",
        "}\n",
        "# Create DataFrame\n",
        "df = pd.DataFrame(data)\n",
        "# Compute Total column\n",
        "df[\"Total\"] = df[\"Quantity\"] * df[\"Price\"]\n",
        "print(df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ttS6s9fwlXHN",
        "outputId": "d88165e4-8a95-4b69-adcc-59a0fcd52135"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID     Product     Category  Quantity  Price Customer Region  Total\n",
            "0      1001      Laptop  Electronics         2    800    Alice  North   1600\n",
            "1      1002       Mouse  Accessories         5     20      Bob  South    100\n",
            "2      1003    Keyboard  Accessories         3     50  Charlie   East    150\n",
            "3      1004     Monitor  Electronics         4    200    Diana   West    800\n",
            "4      1005      Laptop  Electronics         1    850    Ethan  North    850\n",
            "5      1006  Headphones  Accessories         6     40    Fiona  South    240\n",
            "6      1007       Mouse  Accessories        10     25   George   East    250\n",
            "7      1008       Chair    Furniture         2    150   Hannah   West    300\n",
            "8      1009        Desk    Furniture         1    300      Ian  North    300\n",
            "9      1010      Laptop  Electronics         3    900     Jane  South   2700\n",
            "10     1011     Printer  Electronics         2    120     Kyle   East    240\n",
            "11     1012    Keyboard  Accessories         4     55    Laura   West    220\n",
            "12     1013     Monitor  Electronics         2    250     Mike  North    500\n",
            "13     1014       Mouse  Accessories         7     20     Nina  South    140\n",
            "14     1015      Laptop  Electronics         5    750    Oscar   East   3750\n",
            "15     1016  Headphones  Accessories         3     35     Paul   West    105\n",
            "16     1017        Desk    Furniture         2    280    Queen  North    560\n",
            "17     1018     Monitor  Electronics         4    220   Robert  South    880\n",
            "18     1019     Printer  Electronics         1    110    Sarah   East    110\n",
            "19     1020       Chair    Furniture         6    180      Tom   West   1080\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Data Frame 2\n",
        "\n",
        "import pandas as pd\n",
        "# Step 1: Create DataFrame\n",
        "data = {\n",
        "# dictionary with OrderID, Product, etc.\n",
        " \"OrderID\": range(1001, 1021),\n",
        "\"Product\": [\n",
        "\"Laptop\", \"Mouse\", \"Keyboard\", \"Monitor\", \"Laptop\",\n",
        "\"Headphones\", \"Mouse\", \"Chair\", \"Desk\", \"Laptop\",\n",
        "\"Printer\", \"Keyboard\", \"Monitor\", \"Mouse\", \"Laptop\",\n",
        "\"Headphones\", \"Desk\", \"Monitor\", \"Printer\", \"Chair\"\n",
        "],\n",
        "\"Category\": [\n",
        "\"Electronics\", \"Accessories\", \"Accessories\", \"Electronics\", \"Electronics\",\n",
        "\"Accessories\", \"Accessories\", \"Furniture\", \"Furniture\", \"Electronics\",\n",
        "\"Electronics\", \"Accessories\", \"Electronics\", \"Accessories\", \"Electronics\",\n",
        "\"Accessories\", \"Furniture\", \"Electronics\", \"Electronics\", \"Furniture\"\n",
        "],\n",
        "\"Quantity\": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],\n",
        "\"Price\": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],\n",
        "\"Customer\": [\n",
        "\"Alice\", \"Bob\", \"Charlie\", \"Diana\", \"Ethan\",\n",
        "\"Fiona\", \"George\", \"Hannah\", \"Ian\", \"Jane\",\n",
        "\"Kyle\", \"Laura\", \"Mike\", \"Nina\", \"Oscar\",\n",
        " \"Paul\", \"Queen\", \"Robert\", \"Sarah\", \"Tom\"\n",
        "],\n",
        "\"Region\": [\n",
        "\"North\", \"South\", \"East\", \"West\", \"North\",\n",
        "\"South\", \"East\", \"West\", \"North\", \"South\",\n",
        "\"East\", \"West\", \"North\", \"South\", \"East\",\n",
        "\"West\", \"North\", \"South\", \"East\", \"West\"\n",
        "]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "# Step 2: Show first 5 rows\n",
        "print(df.head())\n",
        "# Step 3: Print DataFrame shape\n",
        "print(\"Shape:\", df.shape)\n",
        "# Step 4: Show column names\n",
        "print(\"Columns:\", df.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i_ZYlivXm6Jt",
        "outputId": "41ec8e3b-a217-4c5e-98fd-2517c39ab9e2"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OrderID   Product     Category  Quantity  Price Customer Region\n",
            "0     1001    Laptop  Electronics         2    800    Alice  North\n",
            "1     1002     Mouse  Accessories         5     20      Bob  South\n",
            "2     1003  Keyboard  Accessories         3     50  Charlie   East\n",
            "3     1004   Monitor  Electronics         4    200    Diana   West\n",
            "4     1005    Laptop  Electronics         1    850    Ethan  North\n",
            "Shape: (20, 7)\n",
            "Columns: Index(['OrderID', 'Product', 'Category', 'Quantity', 'Price', 'Customer',\n",
            "       'Region'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "npvjZhE6lYNe"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}