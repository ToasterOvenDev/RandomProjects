import java.util.*;
public class GridMap
{
   protected int xCoords;
   protected int yCoords;
   protected int [][] grid; //Coords of objects and characters 0 means empty 1 means full space
   
   public GridMap(int x, int y)
   {
      xCoords = x;
      yCoords = y;
      grid = new int[xCoords][yCoords];
      for(int row = 0; row<grid.length;row++)
      {
         for(int col = 0; col<grid[row].length;col++)
         {
            grid[row][col] = 0; // Default all pos in gird to free
         }
      }
   }
   public GridMap(int[][] grid)
   {
      this.grid = grid;
   }
   
   public boolean placeCharacter(int[] pos)
   {
      if(checkSpace(pos))
      {
         grid[pos[0]][pos[1]] = 1;
         return true;
      }
      else
      {
         return false;
      }
   }
   public boolean checkSpace(int[] pos)
   {
      int x = pos[0];
      int y = pos[1];
      int space = grid[x][y];
      if(space == 0)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public boolean takeSpace(int[] pos, int[] dstPos)
   {
      int x = dstPos[0];
      int y = dstPos[1];
      int oldX = pos[0];
      int oldY = pos[1];
      int space = grid[x][y];
      if(space == 0)
      {
         //Move character and update space to 1
         grid[x][y] = 1;
         grid[oldX][oldY] = 0;
         return true;
      }
      else
      {
         return false;
      }
   }
   public boolean takeSpaces(int[] pos1, int[] pos2) throws MapException
   {
      int x1 = pos1[0];
      int y1 = pos1[1];
      int x2 = pos2[0];
      int y2 = pos2[1];
      if(x1>x2 || y1>y2)
         throw new MapException("Pos 1 must be smaller than Pos 2 in both X and Y coords");
         
      for(int x = x1; x<x2; x++)
      {
         for(int y = y1; y<y2; y++)
         {
            if(grid[x][y] == 1)
            {
               return false;
            }
         }
      }
      
      for(int x = x1; x<x2; x++)
      {
         for(int y = y1; y<y2; y++)
         {
            grid[x][y] = 1;
         }
      }
      
      return true;
   }
   
   public int[] size()
   {
      int [] gridSize = {xCoords, yCoords};
      return gridSize;
   }
   public void newGrid(int[][] newGrid)
   {
      grid = newGrid;
   }
   public int[][] getGrid()
   {
      return grid;
   }
   public void forceEmpty(int[] pos) throws MapException
   {
      int x = pos[0];
      int y = pos[1];
      int space = grid[x][y];
      if(space == 1)
      {
         grid[x][y] = 0;
      }
      else
      {
         throw new MapException("Space already free");
      }
   }
   public void forceSpacesEmpty(int[] pos1, int[] pos2) throws MapException
   {
      int x1 = pos1[0];
      int y1 = pos1[1];
      int x2 = pos2[0];
      int y2 = pos2[1];
      if(x1>x2 || y1>y2)
         throw new MapException("Pos 1 must be smaller than Pos 2 in both X and Y coords");
      
      for(int x = x1; x<x2; x++)
      {
         for(int y = y1; y<y2; y++)
         {
            grid[x][y] = 0;
         }
      }
   }
}