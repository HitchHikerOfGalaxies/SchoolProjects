using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HUD : MonoBehaviour {

    public Sprite[] HealthSprites;

    public Sprite[] EXPSprites;

    public Sprite[] SkillSquareSprites;

    public Image HealthUI;

    public Image EXPUI;

    public Image SkillSquareUI;

    private Player_Movement player;//Allows access to current Health

    private Player_Attack Experience; //Allows access to current EXP

    private Player_Attack Skill; //Allows access to demo lightning skill

    private void Start()
    {
        player = GameObject.FindGameObjectWithTag("Player").GetComponent<Player_Movement>();
        Experience = GameObject.FindGameObjectWithTag("Player").GetComponent<Player_Attack>();
        Skill = GameObject.FindGameObjectWithTag("Player").GetComponent<Player_Attack>();
    }

    private void Update()
    {
        HealthUI.sprite = HealthSprites[player.curHealth];
        EXPUI.sprite = EXPSprites[Experience.Exp];
        SkillSquareUI.sprite = SkillSquareSprites[Skill.SkillTree];
    }
}
