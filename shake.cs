using System;
using System.IO;
using System.Collections.Generic;

public class Shake
{
    private const int BlockSize = 64; // Taille des blocs en octets
    private List<int> originalOrder;

    public string Shake(string filePath)
    {
        byte[] fileBytes = File.ReadAllBytes(filePath);
        List<byte[]> blocks = FonctionDecoupe(fileBytes);
        originalOrder = new List<int>(blocks.Count);
        for (int i = 0; i < blocks.Count; i++)
        {
            originalOrder.Add(i);
        }
        FonctionShake(blocks);

        string shakenFilePath = filePath + ".shaken";
        File.WriteAllBytes(shakenFilePath, Flatten(blocks));

        return shakenFilePath;
    }

    public string UnShake(string filePath)
    {
        byte[] fileBytes = File.ReadAllBytes(filePath);
        List<byte[]> blocks = FonctionDecoupe(fileBytes);
        FonctionUnShake(blocks);

        string unshakenFilePath = filePath + ".unshaken";
        File.WriteAllBytes(unshakenFilePath, Flatten(blocks));

        return unshakenFilePath;
    }

    private List<byte[]> FonctionDecoupe(byte[] fileBytes)
    {
        List<byte[]> blocks = new List<byte[]>();
        for (int i = 0; i < fileBytes.Length; i += BlockSize)
        {
            byte[] block = new byte[Math.Min(BlockSize, fileBytes.Length - i)];
            Array.Copy(fileBytes, i, block, 0, block.Length);
            blocks.Add(block);
        }
        return blocks;
    }

    private void FonctionShake(List<byte[]> blocks)
    {
        Random rng = new Random();
        int n = blocks.Count;
        while (n > 1)
        {
            n--;
            int k = rng.Next(n + 1);
            byte[] value = blocks[k];
            blocks[k] = blocks[n];
            blocks[n] = value;

            int temp = originalOrder[k];
            originalOrder[k] = originalOrder[n];
            originalOrder[n] = temp;
        }
    }

    private void FonctionUnShake(List<byte[]> blocks)
    {
        byte[][] unshakenBlocks = new byte[blocks.Count][];
        for (int i = 0; i < blocks.Count; i++)
        {
            unshakenBlocks[originalOrder[i]] = blocks[i];
        }
        blocks.Clear();
        blocks.AddRange(unshakenBlocks);
    }

    private byte[] Flatten(List<byte[]> blocks)
    {
        byte[] flat = new byte[blocks.Count * BlockSize];
        for (int i = 0; i < blocks.Count; i++)
        {
            Array.Copy(blocks[i], 0, flat, i * BlockSize, blocks[i].Length);
        }
        return flat;
    }
}
