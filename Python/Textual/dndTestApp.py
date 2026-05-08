from textual.app import App, ComposeResult
from textual.containers import Grid,VerticalScroll,HorizontalScroll,HorizontalGroup,VerticalGroup
from textual.reactive import reactive
from textual.widgets import Button,Digits,Footer,Header,Checkbox,Collapsible,ContentSwitcher,Label,Log,Switch,Tabs,Static

skills = {"Acrobatics":"Str","Animal Handling":"Wis","Arcana":"Int","Athletics":"Str","Deception":"Cha","History":"Int","Insight":"Wis","Intimidation":"Cha","Investigation":"Int","Medicine":"Wis","Nature":"Wis","Perception":"Wis","Performance":"Cha","Persuasion":"Cha","Religion":"Int","Sleight of Hand":"Dex","Stealth":"Dex","Survival":"Wis"}
proficiencies = {"Acrobatics":1,"Animal Handling":0,"Arcana":1,"Athletics":0,"Deception":0,"History":1,"Insight":0,"Intimidation":1,"Investigation":1,"Medicine":0,"Nature":1,"Perception":1,"Performance":0,"Persuasion":1,"Religion":0,"Sleight of Hand":2,"Stealth":2,"Survival":1}
gStats = {"Str":"10","Dex":"10","Con":"10","Int":"10","Wis":"10","Cha":"10"}
gGenericInfo = {"Name":"Dargoth the Destroyer","Class":"Rouge","Level":12,"Background":"Outlander","Player Name":"Joe Smith","Race":"Elf","Alignmnet":"Neutral Neutral","Exp":12000}
gCombatInfo = {"HP":8500,"AC":15,"Hit Dice":"12d8","Initiative":3,"Speed":30,"Inspiration":False}
gInventory = ["Short Sword","Long Bow","Leather Armor","Thieves' Tools","Potion of Healing","Rope","Grappling Hook","Torch","Rations","Waterskin","Backpack","Bedroll","Flint and Steel","Map of the local area","50 gold pieces"]

class Statblock(VerticalGroup):
        """A widget to display a single stat and its value."""
        def __init__(self, stat_name: str, stat_num: str):
                super().__init__()
                self.stat_name = stat_name
                self.stat_num = stat_num

        def compose(self) -> ComposeResult:
                yield Digits(self.stat_num, id = self.stat_name)
                yield Label(self.stat_name, classes = "statName")

class StatsDisplay(HorizontalGroup):
        """A widget to display the character's stats."""
        def __init__(self, stats):
                super().__init__()
                self.stats = stats

        def compose(self) -> ComposeResult:
                for statName,statNum in self.stats.items():
                        yield Statblock(statName, statNum)

class GenericInfoDisplay(Grid):
        """"A widget to display generic info about the character, such as name, class, level, etc."""
        def __init__(self,genericInfo):
                super().__init__()
                self.genericInfo = genericInfo
        
        def compose(self) -> ComposeResult:
                for info,value in self.genericInfo.items():
                        if value != str():
                                value = str(value)
                        yield Label(info+": "+value)

class CombatInfoDisplay(Grid):
        """A widget to display combat info about the character, such as HP, AC, etc."""
        def __init__(self,combatInfo):
                super().__init__()
                self.combatInfo = combatInfo

        def compose(self) -> ComposeResult:
                yield Label("HP: "+str(self.combatInfo["HP"])+"/"+str(self.combatInfo["HP"]))
                yield Label("AC: "+str(self.combatInfo["AC"]))
                yield Label("Hit Dice: "+self.combatInfo["Hit Dice"])
                yield Label("Initiative: "+str(self.combatInfo["Initiative"]))
                yield Label("Speed: "+str(self.combatInfo["Speed"])+" ft.")
                yield HorizontalGroup(
                        Label("Inspiration:",id="inspiration"),
                        Switch(self.combatInfo["Inspiration"]),
                        id="inspirationSwitch"
                )

class InventoryScroll(VerticalScroll):
        """A widget to display the character's inventory in a scrollable container."""
        def __init__(self,inventory):
                super().__init__()
                self.inventory = inventory

        def compose(self) -> ComposeResult:
                for item in self.inventory:
                        yield Label(item)
class InventoryDisplay(Grid):
        """A widget to display the character's inventory."""
        def __init__(self,inventory):
                super().__init__(id="inventoryDisplay")
                self.inventory = inventory

        def compose(self) -> ComposeResult:
                with Collapsible(title="Inventory", id="inventoryCollapsible"):
                        yield InventoryScroll(self.inventory)

class SkillsScroll(VerticalScroll):
        """A widget to display the character's skills in a scrollable container."""
        def __init__(self,skills,proficiencies,stats):
                super().__init__()
                self.skills = skills
                self.proficiencies = proficiencies
                self.stats = stats

        def compose(self) -> ComposeResult:
                for skill,stat in self.skills.items():
                        prof = self.proficiencies[skill]
                        statNum = int(self.stats[stat])
                        statMod = (statNum-10)//2
                        if prof == 1:
                                statMod += 2
                        elif prof == 2:
                                statMod += 4
                        yield Label(skill+": "+str(statMod))
class SkillsDisplay(Grid):
        """A widget to display the character's skills."""
        def __init__(self,stats,skills,proficiencies):
                super().__init__(id="skillsDisplay")
                self.stats = stats
                self.skills = skills
                self.proficiencies = proficiencies

        def compose(self) -> ComposeResult:
                with Collapsible(title="Skills", id="skillsCollapsible"):
                        yield SkillsScroll(skills,proficiencies,self.stats)

class DNDApp(App):
        """A Textual test app to see how a DND app would work"""
        CSS_PATH = "dndTestApp.tcss"
        BINDINGS = [("d","toggle_dark","Toggle dark mode"),("i","toggle_inventory","Toggle inventory")]

        def compose(self) -> ComposeResult:
                """Adds wigits"""
                yield Header()
                yield Footer()
                yield StatsDisplay(gStats)
                yield GenericInfoDisplay(gGenericInfo)
                yield CombatInfoDisplay(gCombatInfo)
                yield InventoryDisplay(gInventory)
                yield SkillsDisplay(gStats,skills,proficiencies)

        def on_mount(self) -> None:
               self.title = "Dungeons And Dragons Companion"
               self.sub_title = "Character"
        
        def action_toggle_dark(self) -> None:
                """Action to toggle dark"""
                self.theme = (
                        "textual-dark" if self.theme == "textual-light" else "textual-light"
                )
        def action_toggle_inventory(self) -> None:
                """Action to toggle inventory"""
                self.query_one("#inventoryCollapsible").collapsed = not self.query_one("#inventoryCollapsible").collapsed

if __name__ == "__main__":
    app = DNDApp()
    app.run()