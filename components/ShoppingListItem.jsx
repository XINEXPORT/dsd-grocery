import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';

const ShoppingListItem = ({ items }) => {
  return (
    <View>
      {items.map((item, index) => (
        <View key={index} style={styles.container}>
          <View style={styles.firstSection}>
            <Image
              source={{ uri: item.image || '' }}
              style={styles.productImg}
              resizeMode='cover'
            />
          </View>
          <View style={styles.textSection}>
            <Text style={styles.headingText}>{item.name}</Text>
            <View style={styles.amountContainer}>
              <Text style={styles.amountText}>{item.qty}</Text>
              <Text style={styles.unitText}>{item.unit}</Text>
            </View>
          </View>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    alignItems: 'center',
    borderColor: '#e7e7e7',
    borderWidth: 1,
    backgroundColor: '#fff',
    height: 180,
    marginBottom: 10, // Add margin between items
  },
  firstSection: {
    flexDirection: 'column',
    alignItems: 'center',
    paddingLeft: 5,
  },
  tagImg: {
    height: 40,
    width: 120,
    borderRadius: 10,
    marginBottom: 2,
  },
  productImg: {
    height: 110,
    width: 100,
    marginTop: 2,
    marginBottom: 2,
    borderRadius: 5,
  },
  textSection: {
    flex: 1,
    paddingLeft: 10,
  },
  headingText: {
    fontSize: 25,
    fontWeight: 'bold',
  },
  amountContainer: {
    flexDirection: 'row',
    alignItems: 'baseline',
    paddingTop: 10,
    paddingBottom: 8,
  },
  amountText: {
    fontSize: 20,
  },
  unitText: {
    fontSize: 20,
    marginLeft: 4,
  },
});

export default ShoppingListItem;
