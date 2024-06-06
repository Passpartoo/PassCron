using System;
using System.Security.Cryptography;
using System.Text;

public class FileEncryptor
{
    private EnigmaMachine enigma;

    public FileEncryptor(string password)
    {
        string rotor1 = ComputeSha256Hash(password);
        string rotor2 = Convert.ToBase64String(Encoding.UTF8.GetBytes(password));
        string rotor3 = ReverseString(ComputeSha256Hash(password));

        enigma = new EnigmaMachine(rotor1, rotor2, rotor3);
    }

    public string EncryptFile(string input)
    {
        string output = "";
        foreach (char c in input)
        {
            output += enigma.Encrypt(c);
        }
        return output;
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

public class EnigmaMachine
{
    private string[] rotorSettings;

    public EnigmaMachine(string rotor1, string rotor2, string rotor3)
    {
        this.rotorSettings = new string[] { rotor1, rotor2, rotor3 };
    }

    public char Encrypt(char input)
    {
        // Enigma simplifiée
        int offset = (int)rotorSettings[0][0] - 'A';
        char encrypted = (char)((input - 'A' + offset) % 26 + 'A');
        RotateRotors();
        return encrypted;
    }

    private void RotateRotors()
    {
        string temp = rotorSettings[0];
        rotorSettings[0] = rotorSettings[1];
        rotorSettings[1] = rotorSettings[2];
        rotorSettings[2] = temp;
    }
}
