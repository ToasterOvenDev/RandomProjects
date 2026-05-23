import java.util.*;

public class Character
{
   // Stats
   protected int str = 10; // Strength
   protected int dex = 10; // Dexterity
   protected int con = 10; // Constitiution
   protected int intl = 10; // Intelligence
   protected int wis = 10; // Wisdom
   protected int chs = 10; // Charisma
   // Stat Modifiers
   protected int smod = calcMod(str);
   protected int dmod = calcMod(dex);
   protected int cmod = calcMod(con);
   protected int imod = calcMod(intl);
   protected int wmod = calcMod(wis);
   protected int chmod = calcMod(chs);
   
   // Level and Class
   protected String characterClass = "N/A";
   protected int level = 0;
   
   // Skills
   protected int proficiency = calcProf(level);
   protected int expertise = proficiency*2;
   
   protected int acrobatics = dmod;
   protected int animalHandling = wmod;
   protected int arcana = imod;
   protected int athletics = smod;
   protected int deception = chmod;
   protected int history = imod;
   protected int insight = wmod;
   protected int intimidation = chmod;
   protected int investigation = imod;
   protected int medicine = wmod;
   protected int nature = imod;
   protected int perception = wmod;
   protected int performance = chmod;
   protected int persuasion = chmod;
   protected int religion = imod;
   protected int slightOfHand = dmod;
   protected int stealth = dmod;
   protected int survival = wmod;
   //Other Important Stuff
      // Inventory
   protected HashMap<String,String> inv = new HashMap<String,String>(); // Stores a list of objects mapped name/desc
         //Inventory functions
   public int invSize()
   {
      return inv.size();
   }
   public void storeItem(String item, String desc)
   {
      inv.put(item,desc);
   }
   
   public void removeItem(String item)
   {
      inv.remove(item);
   }
   
   public String getItem(String item)
   {
      return inv.get(item);
   }
   public void clrInv()
   {
      inv.clear();
   }
      //Combat
   protected boolean inCombat = false;
   protected int [] combatPos;
         //Combat meathods
   public int[] getPos()
   {
      if(inCombat)
         return combatPos;
      else
         return null;
   }
   public boolean getCombatStatus()
   {
      return inCombat;
   }
   public void setCombatStatus(boolean tf)
   {
      inCombat = tf;
   }
   
   // Functions
   private int calcProf(int lvl)
   {
      int prof = (lvl/4)+2;
      if(lvl>=17)
      {
         prof = 6;
      }
      return prof;
   }
   private int calcMod(int stat)
   {
      return (stat - 10)/2;
   }
   
   public Character(int s, int d, int co, int i, int w, int ch) throws CCException
   {
      int sum = s + d + co + i + w + ch;
      if(sum != 60)
         throw new CCException("Sum of stats is not equal to 60!");
      str = s;
      dex = d;
      con = co;
      intl = i;
      wis = w;
      chs = ch;
      
      smod = calcMod(str);
      dmod = calcMod(dex);
      cmod = calcMod(con);
      imod = calcMod(intl);
      wmod = calcMod(wis);
      chmod = calcMod(chs);
      
      acrobatics = dmod;
      animalHandling = wmod;
      arcana = imod;
      athletics = smod;
      deception = chmod;
      history = imod;
      insight = wmod;
      intimidation = chmod;
      investigation = imod;
      medicine = wmod;
      nature = imod;
      perception = wmod;
      performance = chmod;
      persuasion = chmod;
      religion = imod;
      slightOfHand = dmod;
      stealth = dmod;
      survival = wmod;
      
   }
}