Console.Clear();
Console.Write("Введите элементы массива через запятую: ");
string input = Console.ReadLine();
string[] inputArray = input.Split(',');

for (int i = 0; i < inputArray.Length; i++)
{
    inputArray[i] = inputArray[i].Trim();
}

string[] FilterArray(string[] inputArray)
{
    int count = 0;
    int length = inputArray.Length;


    for (int i = 0; i < length; i++)
    {
        if (inputArray[i].Length <= 3)
        {
            count++;
        }
    }

    string[] result = new string[count];
    int index = 0;

    for (int i = 0; i < length; i++)
    {
        if (inputArray[i].Length <= 3)
        {
            result[index] = inputArray[i];
            index++;
        }
    }
    return result;
}

string[] result = FilterArray(inputArray);

Console.WriteLine("Результат:");
Console.WriteLine("[" + string.Join(", ", result) + "]");