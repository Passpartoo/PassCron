using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

public class Enigma
{
    private string rotor1;
    private string rotor2;
    private string rotor3;

    public Enigma(string password)
    {
        rotor1 = ComputeSha256Hash(password);
        rotor2 = Convert.ToBase64String(Encoding.UTF8.GetBytes(password));
        rotor3 = ReverseString(ComputeSha256Hash(password));
    }

    public string Encrypt(string inputFile)
    {
        string output = "";
        string input = File.ReadAllText(inputFile);

        for (int i = 0; i < input.Length; i++)
        {
            char c = input[i];
            c = Rotate(c, rotor1);
            c = Rotate(c, rotor2);
            c = Rotate(c, rotor3);
            output += c;
        }

        string encryptedFilePath = inputFile + ".enigma";
        File.WriteAllText(encryptedFilePath, output);

        return encryptedFilePath;
    }

    private char Rotate(char c, string rotor)
    {
        int offset = rotor[0] % 26;
        c = (char)((c - 'A' + offset) % 26 + 'A');
        rotor = rotor.Substring(1) + rotor[0];
        return c;
    }

    private static string ComputeSha256Hash(string rawData)
    {
        using (SHA256 sha256Hash = SHA256.Create())
        {
            byte[] bytes = sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(rawData));

            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < bytes.Length; i++)
            {
                builder.Append(bytes[i].ToString("x2"));
            }
            return builder.ToString();
        }
    }

    private static string ReverseString(string s)
    {
        char[] arr = s.ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}
