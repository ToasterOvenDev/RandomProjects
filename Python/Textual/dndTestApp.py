from textual.app import App, ComposeResult
from textual.containers import Grid,VerticalScroll,HorizontalScroll,HorizontalGroup,VerticalGroup
from textual.reactive import reactive
from textual.widgets import Button,Digits,Footer,Header,Checkbox,Collapsible,ContentSwitcher,Label,Log,Switch,Tabs,Static

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
        stats = {"Str":"10","Dex":"10","Con":"10","Int":"10","Wis":"10","Cha":"10"}
        def compose(self) -> ComposeResult:
                for statName,statNum in self.stats.items():
                        yield Statblock(statName, statNum)

class GenericInfoDisplay(Grid):
        """"A widget to display generic info about the character, such as name, class, level, etc."""
        def compose(self) -> ComposeResult:
                yield Label("Name: Dargoth the Destroyer")
                yield Label("Class: Rouge")
                yield Label("Level: 12")
                yield Label("Background: outlander")
                yield Label("Player Name: Joe Smith")
                yield Label("Race: Elf")
                yield Label("Alignment: Nuetral Nuetral")
                yield Label("Experience Points: 12000")

class CombatInfoDisplay(Grid):
        """A widget to display combat info about the character, such as HP, AC, etc."""
        def compose(self) -> ComposeResult:
                yield Label("HP: 85/85")
                yield Label("AC: 15")
                yield Label("Hit Dice: 12d8")
                yield Label("Initiative: +3")
                yield Label("Speed: 30 ft.")
                yield HorizontalGroup(
                        Label("Inspiration:",id="inspiration"),
                        Switch(),
                        id="inspirationSwitch"
                )
class InventoryDisplay(Grid):
        """A widget to display the character's inventory."""
        def compose(self) -> ComposeResult:
                with Collapsible(title="Inventory", id="inventoryCollapsible"):
                        yield VerticalScroll(
                                Label("Short Sword"),
                                Label("Long Bow"),
                                Label("Leather Armor"),
                                Label("Thieves' Tools"),
                                Label("Potion of Healing"),
                                Label("Rope"),
                                Label("Grappling Hook"),
                                Label("Torch"),
                                Label("Rations"),
                                Label("Waterskin"),
                                Label("Backpack"),
                                Label("Bedroll"),
                                Label("Flint and Steel"),
                                Label("Map of the local area"),
                                Label("50 gold pieces"),
                                id="inventoryScroll",
                        )

class DNDApp(App):
        """A Textual test app to see how a DND app would work"""
        CSS_PATH = "dndTestApp.tcss"
        BINDINGS = [("d","toggle_dark","Toggle dark mode")]

        def compose(self) -> ComposeResult:
                """Adds wigits"""
                yield Header()
                yield Footer()
                yield StatsDisplay()
                yield GenericInfoDisplay()
                yield CombatInfoDisplay()
                yield InventoryDisplay()

        def on_mount(self) -> None:
               self.title = "Dungeons And Dragons Companion"
               self.sub_title = "Character"
        
        def action_toggle_dark(self) -> None:
                """Action to toggle dark"""
                self.theme = (
                        "textual-dark" if self.theme == "textual-light" else "textual-light"
                )

if __name__ == "__main__":
    app = DNDApp()
    app.run()