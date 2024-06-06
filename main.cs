using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Veuillez entrer le chemin du fichier : ");
        string filePath = Console.ReadLine();

        Console.Write("Veuillez entrer le mot de passe : ");
        string password = Console.ReadLine();

        // Vérifiez que le fichier existe
        if (!File.Exists(filePath))
        {
            Console.WriteLine("Le fichier spécifié n'existe pas.");
            return;
        }

        // Créez des instances de vos classes
        var shake = new Shake();
        var aesEncrypt = new AesEncrypt();
        var enigma = new Enigma(password);

        // Appliquez les transformations
        string shakenFilePath = shake.Shake(filePath);
        string aesEncryptedFilePath = aesEncrypt.Encrypt(shakenFilePath, password);
        string finalFilePath = enigma.Encrypt(aesEncryptedFilePath);

        Console.WriteLine($"Le fichier a été chiffré et est disponible à : {finalFilePath}");
    }
}
