using System;
using System.IO;
using System.Security.Cryptography;

/*
Chiffre le fichier d’entrée en utilisant l’algorithme AES et écrit le résultat dans le fichier de sortie.
La méthode GenerateRandomSalt est utilisée pour générer un sel aléatoire pour le chiffrement.
*/

public class FileEncryptor
{
    public static void EncryptFile(string inputFile, string outputFile, string password)
    {
        byte[] salt = GenerateRandomSalt();
        FileStream fsCrypt = new FileStream(outputFile, FileMode.Create);

        RijndaelManaged AES = new RijndaelManaged();
        AES.KeySize = 256;
        AES.BlockSize = 128;

        var key = new Rfc2898DeriveBytes(password, salt, 50000);
        AES.Key = key.GetBytes(AES.KeySize / 8);
        AES.IV = key.GetBytes(AES.BlockSize / 8);

        AES.Mode = CipherMode.CBC;

        fsCrypt.Write(salt, 0, salt.Length);

        CryptoStream cs = new CryptoStream(fsCrypt, AES.CreateEncryptor(), CryptoStreamMode.Write);

        FileStream fsIn = new FileStream(inputFile, FileMode.Open);

        byte[] buffer = new byte[1048576];
        int read;

        try
        {
            while ((read = fsIn.Read(buffer, 0, buffer.Length)) > 0)
            {
                cs.Write(buffer, 0, read);
            }

            fsIn.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
        finally
        {
            cs.Close();
            fsCrypt.Close();
        }
    }

    public static byte[] GenerateRandomSalt()
    {
        byte[] data = new byte[32];

        using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
        {
            for (int i = 0; i < 10; i++)
            {
                rng.GetBytes(data);
            }
        }

        return data;
    }
}
