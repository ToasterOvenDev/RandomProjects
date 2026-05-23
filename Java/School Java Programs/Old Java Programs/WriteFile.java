import java.nio.file.*;
import java.io.*;

public class WriteFile
{
   public static void main(String [] args) throws IOException
   {
      Path file = Paths.get("OutputFile.txt");
      OutputStream output = null;
      byte [] data;
      String str = "Today is 18 of Feburary 2026";
      
      output = Files.newOutputStream(file);
      output = new BufferedOutputStream(output);
      
      data = str.getBytes();
      output.write(data);
      
      output.flush();
      output.close();
   }
}