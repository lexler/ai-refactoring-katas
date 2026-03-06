package shelflife;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.*;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class InventoryAdjustTest {
    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();
    private final PrintStream standardOut = System.out;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStreamCaptor));
    }

    @AfterEach
    public void tearDown() {
        System.setOut(standardOut);
    }

    @Test
    public void testNormalItem_QualityDecreasesBy1_BeforeSellDate() {
        Item[] items = {new Item("Normal Item", 10, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(19, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testNormalItem_QualityDecreasesBy2_AfterSellDate() {
        Item[] items = {new Item("Normal Item", 0, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(18, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testNormalItem_QualityNeverNegative() {
        Item[] items = {new Item("Normal Item", 10, 0)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(0, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testNormalItem_QualityNeverNegative_AfterSellDate() {
        Item[] items = {new Item("Normal Item", 0, 1)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(0, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testNormalItem_SellInDecreases() {
        Item[] items = {new Item("Normal Item", 5, 10)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(4, items[0].sellIn);
        assertTrue(outputStreamCaptor.toString().contains("Sell-in for Normal Item is now 4"));
    }

    @Test
    public void testCheddarCheese_QualityIncreasesBy1_BeforeSellDate() {
        Item[] items = {new Item("Cheddar Cheese", 10, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(21, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testCheddarCheese_QualityIncreasesBy2_AfterSellDate() {
        Item[] items = {new Item("Cheddar Cheese", 0, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(22, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testCheddarCheese_QualityNeverExceeds50_BeforeSellDate() {
        Item[] items = {new Item("Cheddar Cheese", 10, 50)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testCheddarCheese_QualityNeverExceeds50_AfterSellDate() {
        Item[] items = {new Item("Cheddar Cheese", 0, 50)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testCheddarCheese_QualityApproaches50_AfterSellDate() {
        Item[] items = {new Item("Cheddar Cheese", 0, 49)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testCheddarCheese_LogsQualityChanges() {
        Item[] items = {new Item("Cheddar Cheese", 10, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        String output = outputStreamCaptor.toString();
        assertTrue(output.contains("Quality for Cheddar Cheese is now 21"));
        assertTrue(output.contains("Sell-in for Cheddar Cheese is now 9"));
    }

    @Test
    public void testConcertTickets_QualityIncreasesBy1_MoreThan10DaysOut() {
        Item[] items = {new Item("Concert Tickets", 15, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(21, items[0].quality);
        assertEquals(14, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityIncreasesBy2_10DaysOrLess() {
        Item[] items = {new Item("Concert Tickets", 10, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(22, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityIncreasesBy3_5DaysOrLess() {
        Item[] items = {new Item("Concert Tickets", 5, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(23, items[0].quality);
        assertEquals(4, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityDropsToZero_AfterConcert() {
        Item[] items = {new Item("Concert Tickets", 0, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(0, items[0].quality);
        assertEquals(-1, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityNeverExceeds50_MoreThan10DaysOut() {
        Item[] items = {new Item("Concert Tickets", 15, 50)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(14, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityNeverExceeds50_10DaysOrLess() {
        Item[] items = {new Item("Concert Tickets", 10, 49)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(9, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_QualityNeverExceeds50_5DaysOrLess() {
        Item[] items = {new Item("Concert Tickets", 5, 48)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(50, items[0].quality);
        assertEquals(4, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_LogsMultipleQualityChanges() {
        Item[] items = {new Item("Concert Tickets", 5, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        String output = outputStreamCaptor.toString();
        assertTrue(output.contains("Quality for Concert Tickets is now 21"));
        assertTrue(output.contains("Quality for Concert Tickets is now 22"));
        assertTrue(output.contains("Quality for Concert Tickets is now 23"));
        assertTrue(output.contains("Sell-in for Concert Tickets is now 4"));
    }

    @Test
    public void testConcertTickets_Boundary11Days() {
        Item[] items = {new Item("Concert Tickets", 11, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(21, items[0].quality);
        assertEquals(10, items[0].sellIn);
    }

    @Test
    public void testConcertTickets_Boundary6Days() {
        Item[] items = {new Item("Concert Tickets", 6, 20)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(22, items[0].quality);
        assertEquals(5, items[0].sellIn);
    }

    @Test
    public void testMagicRing_QualityNeverChanges() {
        Item[] items = {new Item("Magic Ring", 10, 80)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(80, items[0].quality);
        assertEquals(10, items[0].sellIn);
    }

    @Test
    public void testMagicRing_SellInNeverChanges() {
        Item[] items = {new Item("Magic Ring", 0, 80)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(80, items[0].quality);
        assertEquals(0, items[0].sellIn);
    }

    @Test
    public void testMagicRing_NoLogging() {
        Item[] items = {new Item("Magic Ring", 10, 80)};
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        String output = outputStreamCaptor.toString();
        assertFalse(output.contains("Magic Ring"));
    }

    @Test
    public void testMultipleItems_AllTypesProcessedCorrectly() {
        Item[] items = {
            new Item("Normal Item", 10, 20),
            new Item("Cheddar Cheese", 5, 10),
            new Item("Concert Tickets", 5, 30),
            new Item("Magic Ring", 0, 80)
        };
        InventoryAdjust app = new InventoryAdjust(items);

        app.updateQuality();

        assertEquals(19, items[0].quality);
        assertEquals(9, items[0].sellIn);

        assertEquals(11, items[1].quality);
        assertEquals(4, items[1].sellIn);

        assertEquals(33, items[2].quality);
        assertEquals(4, items[2].sellIn);

        assertEquals(80, items[3].quality);
        assertEquals(0, items[3].sellIn);
    }

    @Test
    public void testEmptyArray_NoErrors() {
        Item[] items = {};
        InventoryAdjust app = new InventoryAdjust(items);

        assertDoesNotThrow(() -> app.updateQuality());
    }
}
