package shelflife;

public class InventoryAdjust {
    Item[] items;

    public InventoryAdjust(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (int i = 0; i < items.length; i++) {
            if (!items[i].name.equals("Cheddar Cheese")
                    && !items[i].name.equals("Concert Tickets")) {
                if (items[i].quality > 0) {
                    if (!items[i].name.equals("Magic Ring")) {
                        items[i].quality = items[i].quality - 1;
                    }
                }
            } else {
                if (items[i].quality < 50) {
                    items[i].quality = items[i].quality + 1;
                    Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);

                    if (items[i].name.equals("Concert Tickets")) {
                        if (items[i].sellIn < 11) {
                            if (items[i].quality < 50) {
                                items[i].quality = items[i].quality + 1;
                                Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);
                            }
                        }

                        if (items[i].sellIn < 6) {
                            if (items[i].quality < 50) {
                                items[i].quality = items[i].quality + 1;
                                Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);
                            }
                        }
                    }
                }
            }

            if (!items[i].name.equals("Magic Ring")) {
                items[i].sellIn = items[i].sellIn - 1;
                Logger.log("Sell-in for " + items[i].name + " is now " + items[i].sellIn);
            }

            if (items[i].sellIn < 0) {
                if (!items[i].name.equals("Cheddar Cheese")) {
                    if (!items[i].name.equals("Concert Tickets")) {
                        if (items[i].quality > 0) {
                            if (!items[i].name.equals("Magic Ring")) {
                                items[i].quality = items[i].quality - 1;
                                Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);
                            }
                        }
                    } else {
                        items[i].quality = items[i].quality - items[i].quality;
                        Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);
                    }
                } else {
                    if (items[i].quality < 50) {
                        items[i].quality = items[i].quality + 1;
                        Logger.log("Quality for " + items[i].name + " is now " + items[i].quality);
                    }
                }
            }
        }
    }
}
