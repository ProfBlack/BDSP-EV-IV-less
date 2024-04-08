# BDSP EV/IV-less
A script for removing EVs and IVs from trainer teams as well as EV Yields from Pokémon battles. Compatible with any mod but if you are looking for premade patches for the vanilla game or Luminescent Platinum, click [here](https://www.nexusmods.com/pokemonbdsp/mods/17).

# Prerequisites
- [Imposter's Ordeal](https://github.com/Nifyr/Imposters-Ordeal)

# How to use
1. Familiarise yourself with Imposter's Ordeal's usage instructions. Launch it and load your game dump.
	(Optional) Add Mod(s)
2. Select the JSON Converter. Export Pokémon and Trainers to the Input folder of EV/IV-less.
3. Double click Eevee.exe.
4. Appreciate DJ and select any of the options provided.
5. Use Imposter's Ordeal's JSON Converter to import the modified Pokémon and Trainers jsons that are now in the Output folder of EV/IV-less.
6. Close the JSON Converter and select Export and Exit. The Output folder of Imposter's Ordeal will contain your new mod.
	(Optional) If you added mods then all of the files contained within them will be included in the output. The process of removing EVs and IVs only affects two files however. These are:
	1. romfs\Data\StreamingAssets\AssetAssistant\Dpr\**masterdatas**
	2. romfs\Data\StreamingAssets\AssetAssistant\Pml\**personal_masterdatas**
	You can create a small EV/IV-less patch for your mod with just these two files so long as you maintain the folder hierarchy.