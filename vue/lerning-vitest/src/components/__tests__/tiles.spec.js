import { spyOn } from "@vitest/spy";
import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import Tiles from '../Tiles.vue';

describe('tiles', () => {
  it('change tileSelectedIndex on tile click', async () => {
    const wrapper = mount(Tiles);

    const aux = '01234';
    for (let index of aux) {
      index = Number(index);
      await wrapper.find(`#tile-button-${index}`).trigger('click');
      expect(wrapper.vm.tileSelectedIndex).toBe(index);
    }
  });
});

describe('interaction tiles - keydown', () => {
  it('if keydown is letter -> tile receives value', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles)

    const alphabetic = 'abcdefghijklmnopqrstuvwxyz';
    for (let letter of alphabetic) {
      wrapper.vm.tileSelectedIndex = 0;
      await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: letter });
      expect(updateTile).toHaveBeenCalled()
      expect(wrapper.vm.guessedWord).toBe(`${letter}####`);
    }
  });

  it('if keydown is not letter -> tile does not receive value', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles)

    const nonAlphabetic = '1234567890!@#$%^&*()_+=-';
    for (let letter of nonAlphabetic) {
      wrapper.vm.tileSelectedIndex = 0;
      await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: letter });
      expect(updateTile).toHaveBeenCalled()
      expect(wrapper.vm.guessedWord).toBe('#####');
    }
  });
});

describe('change selected tile after letter input', () => {
  it('when all empty and is not the last - go to next', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    const notLastTile = '0123';
    for (let tileIndex in notLastTile) {
      tileIndex = Number(tileIndex);
      await wrapper.setData({ guessedWord: '#####' });
      await wrapper.setData({ tileSelectedIndex: tileIndex});

      await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'a' });
      expect(updateTile).toHaveBeenCalled()
      expect(wrapper.vm.tileSelectedIndex).toBe(tileIndex + 1);
    }
  })

  it('when all empty and is the last - go to first', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: '#####' });
    await wrapper.setData({ tileSelectedIndex: wrapper.vm.guessedWord.length - 1});

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'a' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(0);
  })

  it('jump to next when next already has value', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: '#a###' });
    await wrapper.setData({ tileSelectedIndex: 0 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'a' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(2);
  })

  /*
  todo: make this test works

  it('jump to next when next already has value - advanced', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: 'a####' });
    await wrapper.setData({ tileSelectedIndex: 4 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'a' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(1);
  })
  */

  it('if all tiles filled -> index null', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: 'aaaaa' });
    await wrapper.setData({ tileSelectedIndex: 0 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'a' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(null);
  })
});

describe('change selected tile after backspace', () => {
  it('when tile is filled -> erase content and stay', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: 'a####' });
    await wrapper.setData({ tileSelectedIndex: 0 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'Backspace' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(0);
    expect(wrapper.vm.guessedWord).toBe('#####');
  })

  it('when tile is not first and is empty -> go to previous and erase content', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: 'aa#aa'});
    await wrapper.setData({ tileSelectedIndex: 2 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'Backspace' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(1);
    expect(wrapper.vm.guessedWord).toBe('a##aa');
    
  })

  it('when tile is first and is empty -> go to last and erase content', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: '#aaaa' });
    await wrapper.setData({ tileSelectedIndex: 0 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'Backspace' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(4);
    expect(wrapper.vm.guessedWord).toBe('#aaa#');
    
  })

  it('when all empty and not first -> go to previous tile', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: '#####' });
    await wrapper.setData({ tileSelectedIndex: 2 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'Backspace' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(1);
    expect(wrapper.vm.guessedWord).toBe('#####');
    
  })

  it('when all empty and first -> go to last tile', async () => {
    const updateTile = spyOn(Tiles.methods, 'updateTile');
    const wrapper = mount(Tiles);

    await wrapper.setData({ guessedWord: '#####' });
    await wrapper.setData({ tileSelectedIndex: 0 });

    await wrapper.find(`#tile-button-${wrapper.vm.tileSelectedIndex}`).trigger('keydown', { key: 'Backspace' });
    expect(updateTile).toHaveBeenCalled();
    expect(wrapper.vm.tileSelectedIndex).toBe(4);
    expect(wrapper.vm.guessedWord).toBe('#####');
  })
})
